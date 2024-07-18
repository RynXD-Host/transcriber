const ffmpeg = require('fluent-ffmpeg');
const path = require('path');

// Ambil argumen dari command line
const args = process.argv.slice(2);
if (args.length < 2) {
    console.error('Usage: node convert.js <input.opus> <output.mp3>');
    process.exit(1);
}

const inputFile = args[0];
const outputFile = args[1];

// Fungsi untuk mengonversi opus ke mp3
function convertOpusToMp3(input, output) {
    ffmpeg(input)
        .toFormat('mp3')
        .on('end', () => {
            console.log(`${output}`);
        })
        .on('error', (err) => {
            console.error(err.message);
        })
        .save(output);
}

// Panggil fungsi konversi
convertOpusToMp3(inputFile, outputFile);
