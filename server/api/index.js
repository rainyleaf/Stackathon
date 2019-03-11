const router = require('express').Router()

router.use('/process', require('./process'))

module.exports = router