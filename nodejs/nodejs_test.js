var {PythonShell} = require('python-shell');


var options = {

  mode: 'text',

  //pythonPath: '/usr/bin/python2.7',
  pythonPath: '',

  pythonOptions: ['-u'],

  scriptPath: '',

  args: ['value1', 'value2', 'value3']

};


PythonShell.run('../Raspberry-Face-Recognition-master/face_recognition2.py', options, function (err, results) {

  if (err) throw err;


  console.log('results: %j', results);

});
