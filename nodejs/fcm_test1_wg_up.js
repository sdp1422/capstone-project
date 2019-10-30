var FCM = require('fcm-node');

var serverKey = 'AAAAyW2dkpk:APA91bHWFYE4xIDX9JOWix6SKukgeH-AWfTrBe9b3G-XNO-9V0uNc-L6ngEQ929HEFB1r1G_KBbagdVSR895cMOg3KErvJR_jG7yQvVu5w1rr310u6ynyi_dg7CSYNtpgrh82q5hJhin';

//var client_token = 'dLjdqzaPDzE:APA91bFTDWKpFiAPIYEbA_zYNwMefp46o5rEDSbNnxpgI1A0oTsGMrKllqeGzx47Eq4upZhYz5GoQIbljYLJmj4GIrJ5WFGDED5_ns3IAQus1abIw5wYCVqeFbS1aq_tmP2xD7KCXtz-';

var client_token = 'c2EReyBlNEw:APA91bFu50rPi8oOgaM0SrdMsvLPsovjA3depeYws2lmRm1A1JSxFJUiKHjVDCkUKbXq3A4vOgnRKFJqNR3AdSjP1io2jMI8evbU-n7T7SzhVxD1I6n2i5hd6_4CoJlaEjsxN5dGTwuf';

//var client_token = 'AIzaSyAwnO1K_FmNMz0w2zOMEaoWtyWKNXPeHgA';

var push_data = {
	to: client_token,

	notification: {
		title: "유치원통학버스봇",
		body: "벵거님이 승차하였습니다.",
		sound: "default",
		click_action: "FCM_PLUGIN_ACTIVITY",
		icon: "fcm_push_icon"
	},

	priority: "high",

	//restricted_package_name: "litapps.teliga_bot",
	restricted_package_name: "alessandro.firebaseandroid",

	data: {
		num1:2000,
		num2:3000
	}
};

var fcm = new FCM(serverKey);

fcm.send(push_data, function(err, response) {
	if(err) {
		console.error('Push message error - Arsene up.');
		console.error(err);
		return;
	}

	console.log('Push success - Arsene up.');
	console.log(response);
});
