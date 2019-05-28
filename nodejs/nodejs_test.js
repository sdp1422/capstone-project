var myPythonScriptPath = '../Raspberry-Face-Recognition-master/face_recognition2.py';

// Use python shell
var {PythonShell} = require('python-shell');
var pyshell = new PythonShell(myPythonScriptPath);

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
    console.log(message);
    // console.log(message[0]);
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;
    };

    console.log('finished');
});
