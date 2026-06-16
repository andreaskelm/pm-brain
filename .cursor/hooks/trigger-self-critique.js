// Stop hook: queue end-of-conversation self-critique eval report (draft only).
// Writes a trigger file to system/evals/eval-results/ for the agent or user to process.
// Does NOT auto-apply spec edits (human-gated in v1).

const fs = require('fs');
const path = require('path');

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => { data += chunk; });
    process.stdin.on('end', () => resolve(data));
    process.stdin.on('error', reject);
  });
}

function today() {
  return new Date().toISOString().slice(0, 10);
}

async function main() {
  try {
    const raw = await readStdin();
    if (!raw) return;

    let payload;
    try {
      payload = JSON.parse(raw);
    } catch {
      return;
    }

    if (!payload || payload.status !== 'completed') {
      return;
    }

    const evalDir = path.join(process.cwd(), 'system', 'evals', 'eval-results');
    const date = today();
    const filePath = path.join(evalDir, `self-critique-queue-${date}.md`);

    const lines = [
      `# Self-Critique Queue — ${date}`,
      '',
      `**Queued at:** ${new Date().toISOString()}`,
      '',
      '## Instructions for agent (next turn or /evaluate)',
      '',
      '1. Read the conversation transcript.',
      '2. Apply rubric: `system/evals/judges/self_critique_coaching.md`.',
      '3. Write structured report below this queue entry.',
      '4. **Draft** proposed spec edits with `spec_owner` — do NOT auto-apply.',
      '5. Log PASS/FAIL/MIXED for coaching quality.',
      '',
      '## Report template',
      '',
      '**Verdict:** PASS / FAIL / MIXED',
      '**Sufficiency:** assumptions / know-guess / risk / uncomfortable',
      '**Golden rule:** PASS / FAIL',
      '**Proposed edits (draft):**',
      '- spec_owner: AGENTS.md — ...',
      '',
    ];

    if (!fs.existsSync(evalDir)) {
      fs.mkdirSync(evalDir, { recursive: true });
    }

    if (!fs.existsSync(filePath)) {
      fs.writeFileSync(filePath, lines.join('\n'), { encoding: 'utf8' });
    } else {
      fs.appendFileSync(filePath, `\n---\n\n${lines.slice(2).join('\n')}`, { encoding: 'utf8' });
    }
  } catch {
    // fail open
  }
}

main();
