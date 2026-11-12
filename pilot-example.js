// pilot-example.js — Small example script for the Copilot review pilot
// Purpose: demonstrate a PR with a short, reviewable change.

const fs = require('fs');
const path = require('path');

const cwd = process.cwd();
const files = fs.readdirSync(cwd, { withFileTypes: true });

const summary = files
  .filter(f => f.isFile())
  .map(f => `- ${f.name}`)
  .join('\n');

console.log('Repository files in', cwd + ':');
console.log(summary || '(no files)');

module.exports = { listFiles: () => files };
