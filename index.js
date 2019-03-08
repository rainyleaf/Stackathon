const {exec} = require('child_process')
const empty = require('empty-folder')
const fs = require('fs')
const promisify = require('util.promisify')
const fsPromiseWrite = promisify(fs.writeFile)

let multer  = require('multer');
let express = require('express');
let app     = express();
let upload  = multer({ storage: multer.memoryStorage() });

app.use(express.static('public'))

// app.get('/', (req, res) => {
    
// })

app.post('/single', upload.single('myfile'), (req, res) => {
    const fileObj = req.file
    callPython([fileObj])
    // console.log('req.body: ', req.body);
    // console.log('req.file: ', req.file);
  res.download('./sampledata/fakeOutput.txt');
});

app.post('/array', upload.array('files'), (req, res) => {
    const files = req.files
    callPython(files)
    // console.log('req.body: ', req.body);
    // console.log('req.file: ', req.file);
  res.send();
});

function emptyPromise(...args){
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

// const text1 = 'Dappula tertia is a moth of the Psychidae family. It is widely distributed in the Indo-Australian region, where it is found from India to the Solomon Islands. The habitat consists of lowland areas. The larvae have been recorded feeding on Annona muricata and Cocos nucifera. It can cause damage in Oil Palm and Coffee plantations.'
// const text2 = 'Bucculatrix needhami is a moth in the Bucculatricidae family. It is found in North America, where it has been recorded from Florida, Kentucky, Illinois, Maine, New York, Ohio, South Carolina and Texas. The wingspan is 13–15 mm. The forewings are white marked with irrorated fuscous streaks. The hindwings are pale grey. Adults are on wing from March to July. The larvae feed on Helianthus species. They create a gall, which has the form of a thickening of the walls of the stem. It varies in form from oblong to almost round. Galls mostly occur singly on the stems and are generally located somewhat below mid-height of the plant.'
// const text3 = 'The QRA locator, also called QTH locator in some publications, is an obsolete geographic coordinate system used by amateur radio operators in Europe before the introduction of the Maidenhead Locator System. As a radio transmitter or receiver location system the QRA locator is considered defunct, but may be found in many older documents.'

// const fileObjects = [
//     {buffer: Buffer.from('dummy file', 'utf-8'),
//     filename: 'dummy1.txt'},
//     {buffer: Buffer.from(text1, 'utf-8'),
//     filename: 'Moth1.txt'},
//     {buffer: Buffer.from(text2, 'utf-8'),
//     filename: 'Moth2.txt'},
//     {buffer: Buffer.from(text3, 'utf-8'),
//     filename: 'Radio1.txt'}
// ]

async function tempFilesFromArrayObjs(arrayOfObjs){
    await emptyPromise('./temp', false)
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

async function callPython(fileObjects){
    try {
        await tempFilesFromArrayObjs(fileObjects)
        exec('python3 cleaner_bulk.py', (err, stdout) => {
            if (err){
                console.error(err)
            }
            else {
                console.log(stdout)
            }
        })
    } catch (error) {
        console.error(error)
    }
}

app.listen(8080)
//callPython()
