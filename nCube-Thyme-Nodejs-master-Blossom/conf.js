/**
 * Created by Il Yeup, Ahn in KETI on 2017-02-23.
 */

/**
 * Copyright (c) 2018, OCEAN
 * All rights reserved.
 * Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
 * 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
 * 3. The name of the author may not be used to endorse or promote products derived from this software without specific prior written permission.
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

var ip = require("ip");

var conf = {};
var cse = {};
var ae = {};
var cnt_arr = [];
var sub_arr = [];
var acp = {};

conf.useprotocol = 'mqtt'; // select one for 'http' or 'mqtt' or 'coap' or 'ws'

conf.sim = 'disable'; // enable / disable

// build cse
cse.host        = ' '; //CSE host IP
cse.port        = ' '; //CSE hosting port
cse.name        = 'Mobius';
cse.id          = '/Mobius2';
cse.mqttport    = ' '; //CSE mqtt hosting port
cse.wsport      = ' '; //CSE ws hosting port


// build ae
ae.name         = 'Blossom';
ae.id           = 'S'+ae.name;
ae.parent       = '/' + cse.name;
ae.appid        = 'Blossom';
ae.port         = '9727';
ae.bodytype     = 'json'; // select 'json' or 'xml' or 'cbor'
ae.tasport      = ' '; //CSE tas hosting port




// build cnt
var count = 0;
cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name;
cnt_arr[count].lbl = 'controlTower';
cnt_arr[count++].name = 'controlTower';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name;
cnt_arr[count].lbl = '4WD';
cnt_arr[count++].name = '4WD';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name;
cnt_arr[count].lbl = 'CCTV';
cnt_arr[count++].name = 'CCTV';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name;
cnt_arr[count].lbl = 'edgeDevice';
cnt_arr[count++].name = 'edgeDevice';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[0].name;
cnt_arr[count].lbl = 'escapePath';
cnt_arr[count++].name = 'escapePath';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[0].name;
cnt_arr[count].lbl = 'target';
cnt_arr[count++].name = 'target';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[1].name;
cnt_arr[count].lbl = '4WDcam';
cnt_arr[count++].name = '4WDcam';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[1].name;
cnt_arr[count].lbl = 'motionCapture';
cnt_arr[count++].name = 'motionCapture';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name;
cnt_arr[count].lbl = 'section1';
cnt_arr[count++].name = 'section1';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name;
cnt_arr[count].lbl = 'section2';
cnt_arr[count++].name = 'section2';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name;
cnt_arr[count].lbl = 'section3';
cnt_arr[count++].name = 'section3';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name;
cnt_arr[count].lbl = 'gasSensor';
cnt_arr[count++].name = 'gasSensor';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name;
cnt_arr[count].lbl = 'flameSensor';
cnt_arr[count++].name = 'flameSensor';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name;
cnt_arr[count].lbl = 'room529';
cnt_arr[count++].name = 'room529';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name;
cnt_arr[count].lbl = 'room512';
cnt_arr[count++].name = 'room512';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name;
cnt_arr[count].lbl = 'hall';
cnt_arr[count++].name = 'hall';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name;
cnt_arr[count].lbl = 'room529';
cnt_arr[count++].name = 'room529';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name;
cnt_arr[count].lbl = 'room512';
cnt_arr[count++].name = 'room512';

cnt_arr[count] = {};
cnt_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name;
cnt_arr[count].lbl = 'hall';
cnt_arr[count++].name = 'hall';


// build sub
var count = 0;
sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[0].name + '/' + cnt_arr[4].name;
sub_arr[count].name = 'escapePath';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'escapePath' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http


sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[0].name + '/' + cnt_arr[5].name;
sub_arr[count].name = 'target';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'Blossomtarget' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[1].name + '/' + cnt_arr[6].name;
sub_arr[count].name = '4WDcam';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + '4WDcam' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name + '/' + cnt_arr[8].name;
sub_arr[count].name = 'section1';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'section1' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name + '/' + cnt_arr[9].name;
sub_arr[count].name = 'section2';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'section2' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[2].name + '/' + cnt_arr[10].name;
sub_arr[count].name = 'section3';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'section3' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http


sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name + '/' + cnt_arr[13].name;
sub_arr[count].name = 'room529gas';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room529gas' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name + '/' + cnt_arr[14].name;
sub_arr[count].name = 'room512gas';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room512gas' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[11].name + '/' + cnt_arr[15].name;
sub_arr[count].name = 'hallgas';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room511gas' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name + '/' + cnt_arr[16].name;
sub_arr[count].name = 'room529flame';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room529flame' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name + '/' + cnt_arr[17].name;
sub_arr[count].name = 'room512flame';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room512flame' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http

sub_arr[count] = {};
sub_arr[count].parent = '/' + cse.name + '/' + ae.name + '/' + cnt_arr[3].name + '/' + cnt_arr[12].name + '/' + cnt_arr[18].name;
sub_arr[count].name = 'hallflame';
sub_arr[count++].nu = 'mqtt://' + cse.host + '/' + 'room511flame' + '?ct=' + ae.bodytype; // mqtt
//sub_arr[count++].nu = 'http://' + ip.address() + ':' + ae.port + '/noti?ct=json'; // http



// build acp: not complete
acp.parent = '/' + cse.name + '/' + ae.name;
acp.name = 'acp-' + ae.name;
acp.id = ae.id;


conf.usesecure  = 'disable';

if(conf.usesecure === 'enable') {
    cse.mqttport = '8883';
}

conf.cse = cse;
conf.ae = ae;
conf.cnt = cnt_arr;
conf.sub = sub_arr;
conf.acp = acp;


module.exports = conf;

