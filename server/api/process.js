const router = require('express').Router()
const {exec, execSync} = require('child_process')
const fs = require('fs')
// const promisify = require('util.promisify')
// const fsPromiseWrite = promisify(fs.writeFile)
// const execPromise = promisify(exec)

//route/server stuff
let multer  = require('multer');
let upload  = multer({ storage: multer.memoryStorage() });
//router stuff
router.post('/single', upload.single('file'), (req, res) => {
    try {
        const fileObj = req.file
        //console.log(fileObj)
        let filenames = fs.readdirSync('./server/api/temp')
        for (let filename of filenames) {
            fs.unlinkSync('./server/api/temp/' + filename)
            console.log('deleted ', filename)
        }
        tempFilesFromArrayObjs([fileObj])
        execSync('python3 ./server/api/Lexical-Diversity-master/cleaner_bulk.py', {cwd: null})
        execSync('python3 ./server/api/Lexical-Diversity-master/splitter_bulk.py')
        let tagged = execSync('python3 ./server/api/Lexical-Diversity-master/treetag-batch.py')

        //this is where if-statement logic for a diff copy of the tagged file for each analysis script will go
        fs.writeFileSync(`./server/api/temp/${fileObj.originalname}_tagged_MATTR.txt`, tagged)
        let matt50results = execSync('python3 ./server/api/Lexical-Diversity-master/MATTR_bulk.py 50')
        console.log("results: ", matt50results.toString())
        res.json(matt50results.toString());
    } catch (error) {
        console.error(error)
    }
});

router.post('/array', upload.array('files'), (req, res) => {
    //console.log("in array post route")
    //console.log("req.body: ", req.body)
    try {
        const fileObjs = req.files
        //console.log("fileObjs: ", fileObjs)
        let filenames = fs.readdirSync('./server/api/temp')
        for (let filename of filenames) {
            fs.unlinkSync('./server/api/temp/' + filename)
            console.log('deleted ', filename)
        }
        tempFilesFromArrayObjs(fileObjs)

        execSync('python3 ./server/api/Lexical-Diversity-master/cleaner_bulk.py', {cwd: null})
        execSync('python3 ./server/api/Lexical-Diversity-master/splitter_bulk.py')

        let taggedAll = execSync('python3 ./server/api/Lexical-Diversity-master/treetag-batch.py')
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
            fs.writeFileSync(`./server/api/temp/${arrayOfBuffers[i][0]}_MATTR.txt`, arrayOfBuffers[i][1])
        }

        let matt50results = execSync('python3 ./server/api/Lexical-Diversity-master/MATTR_bulk.py 5000')
        console.log("results: ", matt50results.toString().split('\n'))
        res.json(matt50results.toString().split('\n'));
    } catch (error) {
        console.error(error)
    }
});


function tempFilesFromArrayObjs(arrayOfObjs){
    for (let i = 0; i < arrayOfObjs.length; i++){
        fs.writeFileSync(`./server/api/temp/${arrayOfObjs[i].originalname}`, arrayOfObjs[i].buffer)
    }
}

module.exports = router
