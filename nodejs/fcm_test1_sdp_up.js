var FCM = require('fcm-node');

var serverKey = 'AAAAyW2dkpk:APA91bHWFYE4xIDX9JOWix6SKukgeH-AWfTrBe9b3G-XNO-9V0uNc-L6ngEQ929HEFB1r1G_KBbagdVSR895cMOg3KErvJR_jG7yQvVu5w1rr310u6ynyi_dg7CSYNtpgrh82q5hJhin';

var client_token = 'e32Gvxx090M:APA91bGA8LLICfvLdbRP-fvm7ga5Yb7Sv8Xia0kp_ocjLCaldu5v1prSr5FlTqyC722QCWFJK4YNDIvsNAPSViWYBjdaEPcN8PpUaEojPKEeCXOlqKC3GojhoD3Mcl8gMCemj5_X8wWq';

var push_data = {
	to: client_token,

	notification: {
		title: "title - sdp_up",
		body: "body - sdp_up.",
		sound: "default",
		click_action: "FCM_PLUGIN_ACTIVITY",
		icon: "fcm_push_icon"
	},

	priority: "high",

	restricted_package_name: "alessandro.firebaseandroid",

	data: {
		num1:2000,
		num2:3000
	}
};

var fcm = new FCM(serverKey);

fcm.send(push_data, function(err, response) {
	if(err) {
		console.error('Push Message Failed.');
		console.error(err);
		return;
	}

	console.log('Push Message is sent.');
	console.log(response);
});
