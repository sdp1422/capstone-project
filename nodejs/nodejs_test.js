var {PythonShell} = require('python-shell');


var options = {

  mode: 'text',

  pythonPath: '',

  pythonOptions: ['-u'],

  scriptPath: '',

  args: ['value1', 'value2', 'value3']

};


PythonShell.run('../Raspberry-Face-Recognition-master/test4.py', options, function (err, results) {

  if (err) throw err;


  console.log('results: %j', results);

});
