const {exec} = require('child_process')
const empty = require('empty-folder')
const fs = require('fs')
const promisify = require('util.promisify')
const fsPromiseWrite = promisify(fs.writeFile)
const execPromise = promisify(exec)

//route/server stuff
let multer  = require('multer');
let express = require('express');
let app     = express();
let upload  = multer({ storage: multer.memoryStorage() });

app.use(express.static('public'))

app.post('/single', upload.single('file'), async (req, res) => {
    try {
        const fileObj = req.file
        //Promise.all([clean([fileObj]), split()])
        await clean([fileObj])
        //split()
        res.send();
    } catch (error) {
        console.error(error)
    }
});

app.post('/array', upload.array('files'), (req, res) => {
    const files = req.files
    clean(files)
    res.send();
});


//file processing that is called in routes
function emptyPromise(...args){
    console.log("in emptyer")
    return new Promise(function(resolve, reject){
        empty(...args, ({error, removed, failed}) => {
            if (error){
                reject(error)
            }
            else {
                resolve({removed, failed})
            }
        })
    })
}

async function tempFilesFromArrayObjs(arrayOfObjs){
    await emptyPromise('./temp', false)
    //exec('rm ./temp/*')
    let promises = []
    for (let i = 0; i < arrayOfObjs.length; i++){
        let filepromise = fsPromiseWrite(`temp/${arrayOfObjs[i].originalname}`, arrayOfObjs[i].buffer, function(err){
            if (err){
                console.error(err)
            }
        })
        promises.push(filepromise)
    }
    let done = await Promise.all(promises)
    return done
}

//calling python file-to-file scripts
async function clean(fileObjects){
    await tempFilesFromArrayObjs(fileObjects)
    execPWithErrorCatch('python3 Lexical-Diversity-master/cleaner_bulk.py')
    split()
}

function split(){
    console.log("in split func in js")
    exec('python3 Lexical-Diversity-master/splitter_bulk.py', (err, stdout) => {
        if (err){
            console.error(err)
        }
        else {
            console.log(stdout)
        }
    })}

function execPWithErrorCatch(file){
    execPromise(file, (err, stdout) => {
        if (err){
            console.error(err)
        }
        else {
            console.log(stdout)
        }
    })
}

app.listen(8080)
