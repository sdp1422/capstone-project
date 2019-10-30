var FCM = require('fcm-node');

var serverKey = 'AAAAyW2dkpk:APA91bHWFYE4xIDX9JOWix6SKukgeH-AWfTrBe9b3G-XNO-9V0uNc-L6ngEQ929HEFB1r1G_KBbagdVSR895cMOg3KErvJR_jG7yQvVu5w1rr310u6ynyi_dg7CSYNtpgrh82q5hJhin';

//var client_token = 'dLjdqzaPDzE:APA91bFTDWKpFiAPIYEbA_zYNwMefp46o5rEDSbNnxpgI1A0oTsGMrKllqeGzx47Eq4upZhYz5GoQIbljYLJmj4GIrJ5WFGDED5_ns3IAQus1abIw5wYCVqeFbS1aq_tmP2xD7KCXtz-';

var client_token = 'ed6KBZnxqgY:APA91bFyQx-hs009TJcAK8m5QkrNhTr7mp6uqImKRk0dWVgk9eEp3oX1RF-h7iUkWgdrMXZjoWUMaTve6psjQ_dNw7iNHRd3KHuiSKAMEl0P70ILodIfIj6If4cZtAL1uFrq0Auf8xUU';

var push_data = {
	to: client_token,

	notification: {
		title: "유치원통학버스봇",
		body: "박상돈님이 하차하였습니다.",
		sound: "default",
		click_action: "FCM_PLUGIN_ACTIVITY",
		icon: "fcm_push_icon"
	},

	priority: "high",

	restricted_package_name: "litapps.teliga_bot",

	data: {
		num1:2000,
		num2:3000
	}
};

var fcm = new FCM(serverKey);

fcm.send(push_data, function(err, response) {
	if(err) {
		console.error('Push message error - ParkSangDon down.');
		console.error(err);
		return;
	}

	console.log('Push Success : ParkSangDon down.');
	console.log(response);
});
