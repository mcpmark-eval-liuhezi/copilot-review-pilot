// pilot-example.js
// Small example script for the GitHub Copilot code review pilot.
// Counts words in a short sample text and prints a summary.

const sampleText = "GitHub Copilot code review pilot: a tiny script to demonstrate automated review requests on pull requests.";

function wordCount(text) {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

function main() {
  const words = wordCount(sampleText);
  console.log(`Sample text word count: ${words}`);
  console.log("Pilot example script executed successfully.");
}

main();
