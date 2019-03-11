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

        fs.writeFileSync(`temp/${fileObj.originalname}_tagged_MATTR.txt`, tagged)
        let matt50results = execSync('python3 Lexical-Diversity-master/MATTR_bulk.py 5000')
        console.log("results: ", matt50results.toString())
        res.send();
    } catch (error) {
        console.error(error)
    }
});

app.post('/array', upload.array('files'), (req, res) => {
    console.log("in array post route")
    try {
        const fileObjs = req.files
        console.log("fileObjs: ", fileObjs)
        let filenames = fs.readdirSync('./temp')
        for (let filename of filenames) {
            fs.unlinkSync('./temp/' + filename)
            console.log('deleted ', filename)
        }
        tempFilesFromArrayObjs(fileObjs)

        execSync('python3 Lexical-Diversity-master/cleaner_bulk.py', {cwd: null})
        execSync('python3 Lexical-Diversity-master/splitter_bulk.py')

        let taggedAll = execSync('python3 Lexical-Diversity-master/treetag-batch.py')
        let taggedSplit = taggedAll.toString().split('\n~~~~~~~~~SPLIT~HERE~~~~~~~~~~\n')
        let arrayOfBuffers = []
        for (let j = 0; j + 1 < taggedSplit.length; j++){
            let titleAndText = taggedSplit[j].split('\n~Second-split-here~\n')
            let title = titleAndText[0]
            let buffer = Buffer.from(titleAndText[1], 'utf-8')
            arrayOfBuffers.push([title, buffer])
        }
        for (let i = 0; i < fileObjs.length; i++){
            //this is where if-statement logic for a diff copy of the tagged file for each analysis script will go
            fs.writeFileSync(`temp/${arrayOfBuffers[i][0]}_MATTR.txt`, arrayOfBuffers[i][1])
        }

        let matt50results = execSync('python3 Lexical-Diversity-master/MATTR_bulk.py 5000')
        console.log("results: ", matt50results.toString())
        res.send();
    } catch (error) {
        console.error(error)
    }
});


function tempFilesFromArrayObjs(arrayOfObjs){
    for (let i = 0; i < arrayOfObjs.length; i++){
        fs.writeFileSync(`temp/${arrayOfObjs[i].originalname}`, arrayOfObjs[i].buffer)
    }
}

app.listen(8080)
