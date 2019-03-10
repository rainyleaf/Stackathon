const {exec, execSync} = require('child_process')
const fs = require('fs')
// const promisify = require('util.promisify')
// const fsPromiseWrite = promisify(fs.writeFile)
// const execPromise = promisify(exec)

//route/server stuff
let multer  = require('multer');
let express = require('express');
let app     = express();
let upload  = multer({ storage: multer.memoryStorage() });

app.use(express.static('public'))

app.post('/single', upload.single('file'), (req, res) => {
    try {
        const fileObj = req.file
        let filenames = fs.readdirSync('./temp')
        for (let filename of filenames) {
            fs.unlinkSync('./temp/' + filename)
            console.log('deleted ', filename)
        }
        tempFilesFromArrayObjs([fileObj])
        execSync('python3 Lexical-Diversity-master/cleaner_bulk.py', {cwd: null})
        execSync('python3 Lexical-Diversity-master/splitter_bulk.py')
        let tagged = execSync('python3 Lexical-Diversity-master/treetag-batch.py')
        fs.writeFileSync(`temp/${fileObj.originalname}_tagged.txt`, tagged)
        let matt50results = execSync('python3 Lexical-Diversity-master/MATTR_bulk.py 5000')
        console.log("results: ", matt50results.toString())
        res.send();
    } catch (error) {
        console.error(error)
    }
});

app.post('/array', upload.array('files'), (req, res) => {
    // const files = req.files
    // clean(files)
    res.send();
});


function tempFilesFromArrayObjs(arrayOfObjs){
    for (let i = 0; i < arrayOfObjs.length; i++){
        fs.writeFileSync(`temp/${arrayOfObjs[i].originalname}`, arrayOfObjs[i].buffer)
    }
}

app.listen(8080)
