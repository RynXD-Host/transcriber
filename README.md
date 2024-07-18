<div align="center">

  <img title="Converter" src="https://img.shields.io/badge/Converter-yellow?colorA=%23ff0000&colorB=%23017e40&style=for-the-badge">

</div>

---


<div align="center">  
  <a href="https://github.com/RynXD-Host">
    <img title="RynXD-Host" src="https://img.shields.io/badge/AUTHOR-RynXD-orange.svg?style=for-the-badge&logo=github"></a>
</div>

<br>
<p> Rest API Flask & nodejs for converting audio to text</p>


<p align="center">

**This API Support on :**
</p>

<p align="center">
  <img title="Linux" src="https://img.shields.io/badge/Linux-302c2c?style=for-the-badge&logo=iterm2&logoColor=000000"></img>
  <img title="Docker" src="https://img.shields.io/badge/Docker-302c2c?style=for-the-badge&logo=iterm2&logoColor=000000"></img>
</p>

## Getting Started
This project require :
- [NodeJS](https://nodejs.org/en/download/) [v16 or greater](https://nodejs.org/dist/)
- [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)
- [Python]

## Install

```bash
git clone https://github.com/RynXD-Host/converter
cd converter 
npm install
pip -r install requirements.txt
python app.py
```

## Example Usage

Using Axios

```bash
const axios = require('axios')
const fs = require('fs')
const FormData = require('form-data')

const inputPath = '/path/to/your.opus'
const form = new FormData()
form.append('file', fs.createReadStream(inputPath));

axios.post('http://localhost:7860/upload', form, {
    headers: {
        ...form.getHeaders()
    }
}).then(response => {
console.log(response.data.message)
})
```

## Donate
<a href="https://saweria.co/rynxd" target="_blank"><img src="https://user-images.githubusercontent.com/26188697/180601310-e82c63e4-412b-4c36-b7b5-7ba713c80380.png" alt="Donate For RynXD" height="41" width="174"></a>

## License
[MIT License](https://github.com/RynXD-Host/converter/blob/main/LICENSE)

Copyright (c) 2024 RynXD
