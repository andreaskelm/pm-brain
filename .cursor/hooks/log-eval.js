// Lightweight post-conversation eval logger.
// Reads conversation metadata from stdin and appends a short summary
// to `.cursor/evals/eval-results/auto-[YYYY-MM-DD].md`.
//
// This is intentionally minimal: no external dependencies, no secrets.

const fs = require('fs');
const path = require('path');

function readStdin() {
  return new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', chunk => {
      data += chunk;
    });
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
      // If payload is not JSON, skip logging.
      return;
    }

    if (!payload || payload.status !== 'completed') {
      return;
    }

    const date = today();
    const evalDir = path.join(process.cwd(), '.cursor', 'evals', 'eval-results');
    const filePath = path.join(evalDir, `auto-${date}.md`);

    const summaryLines = [];
    summaryLines.push(`## Conversation - ${new Date().toISOString()}`);
    if (payload.conversationId) {
      summaryLines.push(`**Conversation ID:** ${payload.conversationId}`);
    }
    if (payload.tags && Array.isArray(payload.tags) && payload.tags.length > 0) {
      summaryLines.push(`**Tags:** ${payload.tags.join(', ')}`);
    }
    if (payload.evalCheckpoints && Array.isArray(payload.evalCheckpoints)) {
      summaryLines.push('**Eval Checkpoints Hit:**');
      payload.evalCheckpoints.forEach(cp => {
        summaryLines.push(`- ${cp}`);
      });
    }
    summaryLines.push('');

    const block = summaryLines.join('\n');

    if (!fs.existsSync(evalDir)) {
      fs.mkdirSync(evalDir, { recursive: true });
    }

    if (!fs.existsSync(filePath)) {
      const header = `# Auto Eval Log - ${date}\n\n`;
      fs.writeFileSync(filePath, header + block, { encoding: 'utf8' });
    } else {
      fs.appendFileSync(filePath, block, { encoding: 'utf8' });
    }
  } catch {
    // Swallow errors to avoid breaking the main workflow.
  }
}

main();

