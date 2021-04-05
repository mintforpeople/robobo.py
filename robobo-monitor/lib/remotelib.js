//const WebSocket = require('ws');

/*******************************************************************************
 * Copyright 2018 Mytech Ingenieria Aplicada <http://www.mytechia.com>
 * Copyright 2018 Luis Llamas <luis.llamas@mytechia.com>
 * Copyright 2018 Gervasio Varela <gervasio.varela@mytechia.com>
 * 
 * <p>
 * This file is part of Robobo.js, the Robobo Javascript Programming Library.
 * <p>
 * Robobo.js is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * <p>
 * Robobo.js is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * <p>
 * You should have received a copy of the GNU Lesser General Public License
 * along with Robobo.js.  If not, see <http://www.gnu.org/licenses/lgpl.html>.
 ******************************************************************************/


//Javascript remote control library for the Robobo educational robot - Version 1.0.1-dev

//Constructor of the remote control object
function Remote(ip,passwd){
  this.ip = ip.trim();
  this.port = 40404;

  //Last keep-alive message timestamp
  this.lastKeepAliveTime = 0;
  this.maxKeepAlivePeriod = 1000*1*60; //1 minutes

  //WebSocket to stablish the connection
  this.ws = undefined;

  //Unique command id sent to the server
  this.commandid = 0;

  //Map of statuses
  this.statusmap = new Map();

  //Map of last relevant statuses, for comparations
  this.laststatusmap = new Map();

  //Map of callbacks registered by the extension
  this.callbackmap = new Map();

  this.wheelsCallbackMap = new Map();
  this.tiltCallbackMap = new Map();
  this.panCallbackMap = new Map();

  //Map of blocking callbacks
  //this.blockingcallbackmap = new Map();

  //First execution mark
  this.firstime = true;

  //Connection state
  this.connectionState = Remote.ConnectionStateEnum.DISCONNECTED;

  //Connection password
  this.password = passwd;


  //Wheel stop callback
  this.wheelsCallback = undefined;


  //Wheel degrees stop callback
  this.degreesCallback = undefined;

  //Tilt stop callback
  this.tiltCallback = undefined;

  //Pan stop callback
  this.panCallback = undefined;

  //Speech synthesis callback
  this.talkCallback = undefined;

  //defaults and limits
  this.panSpeedLimit = 40;
  this.tiltSpeedLimit = 10;

  this.wheelsSpeedLimit = 250;

  this.panInferiorLimit =  11;
  this.panSuperiorLimit =  343;

  this.tiltInferiorLimit = 7;
  this.tiltSuperiorLimit = 105;

  this.minIRValue = 20;

  this.lostFace = true;


  this.timeout = 10;
  this.wheelLastTime = Date.now();
  this.panLastTime = Date.now();
  this.tiltLastTime = Date.now();
  
  ;

  

//END OF REMOTE OBJECT
};

//State enumarion fo the connection with the remote robot
Remote.ConnectionStateEnum = {
  CONNECTING: 0,
  CONNECTED: 1,
  RECONNECTING: 2,
  DISCONNECTED: 3
}

//Remote control implementation
Remote.prototype = {


  registerCallback: function (name,callback) {
    this.callbackmap.set(name,callback);
    //END OF REGISTERCALLBACK FUNCTION
  },

  /** Establishes connection with the remote Robobo */
  connect :function() {
    if (this.ws != undefined){
      console.log("Closing previous connection");
      this.ws.close();
      if (this.callbackmap.get("onConnectionChanges")!=undefined){
        (this.callbackmap.get("onConnectionChanges"))(1);
      }
    }

    this.connectionState = Remote.ConnectionStateEnum.CONNECTING;

    this.ws = new WebSocket("ws://"+this.ip+":"+this.port);

    this.ws.onopen = function() {
      console.log("Connection Stablished");
      if (this.callbackmap.get("onConnectionChanges")!=undefined){
        (this.callbackmap.get("onConnectionChanges"))(2);
      }
      this.sendMessage("PASSWORD: "+this.password);
      this.keepAlive();
      this.connectionState = Remote.ConnectionStateEnum.CONNECTED;
    }.bind(this);

    //adds the listener to process incoming messages
    this.ws.addEventListener('message', function(evt) {
      var received_msg = evt.data;
      this.handleMessage(received_msg);
    }.bind(this));

    this.ws.onclose = function(event) {
      var error = false;
      if(this.connectionState != Remote.ConnectionStateEnum.RECONNECTING && 
        this.connectionState != Remote.ConnectionStateEnum.DISCONNECTED){
        var reason;

          // See http://tools.ietf.org/html/rfc6455#section-7.4.1
          if (event.code == 1000)
              reason = "";
          else if(event.code == 1001)
              reason = "";
          else if(event.code == 1002) {
              reason = "Protocol Error";
              error = true;
          }
          else if(event.code == 1003) {
              reason = "Invalid data";
              error = true;
          }
          else if(event.code == 1004)
              reason = "";
          else if(event.code == 1005)
              reason = "";
          else if(event.code == 1006){
             reason = "Lost connection";             
           }
          else if(event.code == 1007)
              reason = "";
          else if(event.code == 1008)
              reason = "";
          else if(event.code == 1009)
             reason = "";
          else if(event.code == 1010) // Note that this status code is not used by the server, because it can fail the WebSocket handshake instead.
              reason = "";
          else if(event.code == 1011)
              reason = "";
          else if(event.code == 1015) {
              reason = "Failure to perform a TLS handshake";
              error = true;
          }
          else {
              reason = "Unknown reason";
              error = true;
          }


          if (error){
            if (this.callbackmap.get("onConnectionChanges")!=undefined){
              (this.callbackmap.get("onConnectionChanges"))(0);
            }
          }else{
            if (this.callbackmap.get("onConnectionChanges")!=undefined){
              (this.callbackmap.get("onConnectionChanges"))(1);
            }
          }

      }      

      this.reconnecting = false;
      console.log("Connection closed because: "+event.code);
      this.connectionState = Remote.ConnectionStateEnum.DISCONNECTED;
    }.bind(this);

    this.ws.onerror = function(error){
      this.connectionState = Remote.ConnectionStateEnum.DISCONNECTED;
      if (this.callbackmap.get("onConnectionChanges")!=undefined){
          (this.callbackmap.get("onConnectionChanges"))(0);
      }
      console.log("Error in websocket connection to Robobo: "+error);
    }.bind(this);

    this.setIRValue('Back-R',0);
    this.setIRValue('Back-C',0);
    this.setIRValue('Front-RR',0);
    this.setIRValue('Front-R',0);
    this.setIRValue('Front-C',0); 
    this.setIRValue('Front-L',0);
    this.setIRValue('Front-LL',0);
    this.setIRValue('Back-L',0);
    this.resetSensors();
  }, //ENDOF connect
  filterMovement(speed,axis){
    if (speed == 0){
      return true;
    }else{
      switch (axis) {
        case "pan":
          return ((Date.now()-this.panLastTime)>this.timeout);
          break;

        case "tilt":
          
          return ((Date.now()-this.tiltLastTime)>this.timeout);
          break;

        case "wheels":
        
          return ((Date.now()-this.wheelLastTime)>this.timeout);
        break;

        default:
          return false;
          break;
      }
    }
  },
  /** Waits until the connection is established */
  waitForConnection : function() {

    var startTime = new Date().getTime();
    while(true) {
      var currentTime = new Date().getTime();
      if (startTime+1000 < currentTime) {
        break;
      }
    }

  }, //ENDOF waitForConnection

  /** Checks whether the connection is established or not */
  isConnected : function() {
    return this.connectionState == Remote.ConnectionStateEnum.CONNECTED;
  },//ENDOF isConnected

  //closeConnection - Closes the connection with the remote Robobo
  closeConnection: function(reconnect) {
    if (reconnect) {
      this.connectionState = Remote.ConnectionStateEnum.RECONNECTING;
    }
    this.ws.close();
  }, //ENDOF closeConnection

  /** Sends a message to the remote Robobo */
  sendMessage: function(message) {
    this.commandid = this.commandid +1;
    this.ws.send(message);

    //ENDOF sendMessage
  },

  /** Notifies an error */
  fireError: function (err) {
    console.log("ERROR "+ err);
    this.statusmap.set("error",err);

    if (this.callbackmap.get("onError") != null) {
      (this.callbackmap.get("onError"))(); 
    }    
  },//ENDOF fireError

  /** Handles and processes an incoming message from the remote Robobo */
  handleMessage: function(message) {

    var jsonmsg = JSON.parse(message)
    //console.log(typeof(jsonmsg.name) == 'string');
    if (typeof(jsonmsg.name) == 'string'){
      this.manageStatus(jsonmsg);
    }else if (typeof(jsonmsg.commandid) != "undefined") {
      this.manageResponse(jsonmsg);
    }

  },//ENDOF handleMessage


  /*********************************/
  /* ROBOT BASE FUNCTIONS *
  /*********************************/
  /** Resets the robot encoder count */
  resetEncoders: function(){
    var message = JSON.stringify({
      "name": "RESET-WHEELS",
      "parameters": {},
      "id": this.commandid
  });
  this.sendMessage(message);
  //ENDOF resetEncoders
  },
  
  /** Commands the robot to move the wheel by some angle */
  moveWheelsByDegree: function(wheel,degrees,speed,callback) {

    if (this.filterMovement(speed,"wheels")){
      this.wheelLastTime = Date.now();
      
      this.wheelsCallbackMap.set(this.commandid+'',callback);

      
      var message = JSON.stringify({
          "name": "MOVEBY-DEGREES",
          "parameters": {
              wheel: wheel,
              degrees: degrees,
              speed:speed,
              blockid:this.commandid
          },
          "id": this.commandid
      });
      this.sendMessage(message);
    }else{
      console.warn('Robobo Warning: Ignored moveWheelsByDegree command. Maybe the client is sending messages too fast?');
      callback();
    }
    
    //ENDOF moveWheelsByDegree
  },


  /** Commands the robot to move during some time */
  moveWheelsByTime: function(wheel,time,speed) {
    if (this.filterMovement(speed,"wheels")){
      this.wheelLastTime = Date.now();
      var message = JSON.stringify({
        "name": "MOVEBY-TIME",
        "parameters": {
            wheel: wheel,
            time: time,
            speed:speed
        },
        "id": this.commandid
    });
    this.sendMessage(message);
  }
    //ENDOF moveWheelsByTime
  },


  /** Commands the robot to move each wheel with an idepenent speed */
  moveWheelsSeparated: function(lSpeed,rSpeed,time) {
    if (this.filterMovement((Math.abs(lSpeed)+Math.abs(rSpeed)),"wheels")){
      this.wheelLastTime = Date.now();
      lS = ''+lSpeed;
      rS = ''+rSpeed;

      var message = JSON.stringify({
          "name": "MOVE",
          "parameters": {
              lspeed: lS,
              rspeed: rS,
              time:time
          },
          "id": this.commandid
      });
      this.sendMessage(message);
  }

  },//ENDOF moveWheelsSeparated


  /** Commands the robot to move each wheel with an idepenent speed and waits
   * until the roboot finishes the movement */
  moveWheelsSeparatedWait: function(lSpeed,rSpeed,time,callback) {
    if (this.filterMovement((Math.abs(lSpeed)+Math.abs(rSpeed)),"wheels")){
      this.wheelLastTime = Date.now();
      //console.log("moveWheelsSeparatedWait "+lSpeed+" "+rSpeed+" "+time);
      lS = ''+lSpeed;
      rS = ''+rSpeed;

      
    
      this.wheelsCallbackMap.set(this.commandid+'',callback);
      var message = JSON.stringify({
          "name": "MOVE-BLOCKING",
          "parameters": {
              lspeed: lS,
              rspeed: rS,
              time:time,
              blockid: this.commandid
          },
          "id": this.commandid
      });
      this.sendMessage(message);
    }else{
      console.warn('Robobo Warning: Ignored moveWheelsByTime command. Maybe the client is sending messages too fast?');

      callback();
    }

  },//ENDOF moveWheelsSeparatedWait


  /** Commands the robot to turn on the wheels motors at the specified speed, indefinitely */
  motorsOn: function(lMotor,rMotor,speed) {
    if (this.filterMovement(speed,"wheels")){
      this.wheelLastTime = Date.now();
      var message = JSON.stringify({
          "name": "MOVE-FOREVER",
          "parameters": {
              lmotor: lMotor,
              rmotor: rMotor,
              speed:speed
          },
          "id": this.commandid
      });
      this.sendMessage(message);
    }

  },//ENDOF MOVE-FOREVER


  /** Commands the robot to turn by some degrees */
  turnInPlace: function(degrees) {
    if (this.filterMovement(speed,"wheels")){
      this.wheelLastTime = Date.now();
      var message = JSON.stringify({
          "name": "TURNINPLACE",
          "parameters": {
              degrees: degrees
          },
          "id": this.commandid
      });
      this.sendMessage(message);
    }

  },//ENDOF turnInPlace


  /** Commands the robot to move the PAN to the specified position */
  movePan: function(pos, vel) {
    if (this.filterMovement(vel,"pan")){
      this.panLastTime = Date.now();
      s = ''+ vel;
      pos = this.scratchToRoboboAngle(pos);
      
      if (pos > this.panSuperiorLimit){
        pos = this.panSuperiorLimit;
      }

      if (pos < this.panInferiorLimit){
        pos = this.panInferiorLimit;
      }
      
      var message = JSON.stringify({
          "name": "MOVEPAN",
          "parameters": {
              pos: pos,
              speed:s
          },
          "id": this.commandid
      });
      //if (vel > 0){
      //  this.statusmap.set("panPos",pos);
      //}
      this.sendMessage(message);
    }

  }, //ENDOF movePan


  /** Commands the robot to move the PAN to the specified position
   * and waits until the movement finishes */
  movePanWait: function(pos, vel, callback) {
    if (this.filterMovement(vel,"pan")){
      this.panLastTime = Date.now();
      s = ''+ vel;
      pos = this.scratchToRoboboAngle(pos);    
      
      if (pos > this.panSuperiorLimit){
        pos = this.panSuperiorLimit;
      }

      if (pos < this.panInferiorLimit){
        pos = this.panInferiorLimit;
      }
      


      this.panCallbackMap.set(this.commandid+'',callback);


      

      var message = JSON.stringify({
          "name": "MOVEPAN-BLOCKING",
          "parameters": {
              pos: pos,
              speed:s,
              blockid:this.commandid
          },
          "id": this.commandid
      });
      //if (vel > 0){
      //  this.statusmap.set("panPos",pos);
      //}
      this.sendMessage(message);
    }else{
      console.warn('Robobo Warning: Ignored movePan command. Maybe the client is sending messages too fast?');
      callback();
    }

  },//ENDOF movePanWait

  /** Returns the current PAN position */
  getPan:function() {
    return this.statusmap.get("panPos")
  },//ENDOF getPan

  /** Returns the current TILT position */
  getTilt:function() {
    return this.statusmap.get("tiltPos")
  },//ENDOF getTilt

  /** Commands the  robot to move the PAN by some degrees */
  movePanByDegrees: function (degrees, speed) {
    if (this.filterMovement(speed,"pan")){
      this.panLastTime = Date.now();
      console.log("movePanByDegrees");
      var actual = this.statusmap.get("panPos");
      if (actual==undefined){
        actual = 180;
      }
      var newpos = parseInt(actual) + parseInt(degrees)
      if (newpos > 339){
        newpos = 339;
      }
      if (newpos < 27){
        newpos = 27;
      }
      console.log(newpos);

      //this.statusmap.set("panPos",parseInt(newpos));
      this.movePan(newpos, speed);
    }
    //END OF MOVEPANBYDEGREES FUNCTION
  },


  /** Commands the robot to move the TILT to an specified position */
  moveTilt: function (pos, vel) {
    if (this.filterMovement(vel,"tilt")){
      this.tiltLastTime = Date.now();
      s = ''+ vel;
  
      

      var message = JSON.stringify({
          "name": "MOVETILT",
          "parameters": {
              pos: pos,
              speed:s
          },
          "id": this.commandid
      });
      //if (vel > 0){
      //  this.statusmap.set("tiltPos",parseInt(pos));
      //}
      this.sendMessage(message);
    }

  },//ENDOF moveTilt


  /** Commands the robot to move the TILT to an specified position
   * and waits until the robot ends the movement */
  moveTiltWait: function (pos, vel, callback) {
    
    if (this.filterMovement(vel,"tilt")){
      this.tiltLastTime = Date.now();
      s = ''+ vel;
      if (pos > this.tiltSuperiorLimit){
        pos = this.tiltSuperiorLimit;
      }

      if (pos < this.tiltInferiorLimit){
        pos = this.tiltInferiorLimit;
      }

      this.tiltCallbackMap.set(this.commandid+'',callback);

      var message = JSON.stringify({
          "name": "MOVETILT-BLOCKING",
          "parameters": {
              pos: pos,
              speed:s,
              blockid:this.commandid
          },
          "id": this.commandid
      });
      //if (vel > 0){
      //  this.statusmap.set("tiltPos",parseInt(pos));
      //}
      this.sendMessage(message);
    }else{
      console.warn('Robobo Warning: Ignored moveTilt command. Maybe the client is sending messages too fast?');
      callback();
    }

  },//ENDOF moveTiltWait


  /** Commands the  robot to move the TILT by some degrees */
  moveTiltByDegrees: function (degrees, speed) {
    if (this.filterMovement(speed,"tilt")){
      this.tiltLastTime = Date.now();
      console.log("moveTiltByDegrees");
      var actual = this.statusmap.get("tiltPos");
      if (actual==undefined){
        actual = 90;
      }
      var newpos = parseInt(actual) + parseInt(degrees)
      if (newpos > 109){
        newpos = 109;
      }
      if (newpos < 26){
        newpos = 26;
      }
      console.log(newpos);
      //this.statusmap.set("tiltPos",newpos);
      this.moveTilt(newpos, speed);
    }

  },//ENDOF moveTiltByDegrees


  /** Returns the last value detected by the infrared senseor specified by 'irnumber' */
  getIRValue : function (ir) {
    return this.statusmap.get(ir);
  },//ENDOF getIRValue

  /** Sets the value of an IR sensor using its key from IRS */
  setIRValue : function(key, value) {
    //console.log(key+' '+value);
    if (value <= this.minIRValue) { //limit the minimun value
      value = 0;
    }

    this.statusmap.set(key,value);
  }, //ENDOF setIRValue


  /** Returns the last value detected by the infrared senseor specified by 'irnumber' */
  getObstacle : function (ir) {
    return this.statusmap.get(ir);
  },


  /** Returns the last known value of Robobo's base battery level */
  checkBatt : function () {
    return this.statusmap.get("batterylevel");
  },//ENDOF checkBatt

  /** Returns the last known position of the specified wheel */
  getWheel : function(wheel, type){
    var value;
    if (type == "speed"){
      if (wheel == "right"){
          value = this.statusmap.get("wheelSpeedR");
      }else{
          value = this.statusmap.get("wheelSpeedL");

      }
    }else{
      if (wheel == "right"){
        value = this.statusmap.get("wheelPosR");

      }else{
        value = this.statusmap.get("wheelPosL");
      }
    }
    return value;
  },

  /** Returns the last know color of the specified led */
  getLedColor : function (led, channel){
      return this.statusmap.get(led+'LED-'+channel);

  },


  /***************************************/
  /* ENDOF ROBOT BASE FUNCTIONS *
  /***************************************/

  //---------------------------------------


  /***************************************/
  /* EMOTION INTERACTION FUNCTIONS   *
  /***************************************/

  /** Commands the robot to change its face/emotion */
  changeEmotion : function (emotion) {
    var message = JSON.stringify({
        "name": "SET-EMOTION",
        "parameters": {
            emotion: emotion
        },
        "id": this.commandid
    });
    this.sendMessage(message);

  }, //ENDOF changeEmotion


  /** Returns the last known Robobo emotion */
  getEmotion : function (){
    return this.statusmap.get("emotion");
  },


  /** Commands the robot to play a prerecorded sound */
  playEmotionSound : function (sound) {
    var message = JSON.stringify({
        "name": "PLAY-SOUND",
        "parameters": {
            sound:sound
        },
        "id": this.commandid
    });
    this.sendMessage(message);

  },//ENDOF playEmotionSound

  /***************************************/
  /* ENDOF EMOTION BASE FUNCTIONS *
  /***************************************/

  //---------------------------------------

  /***************************************/
  /* SOUND-BASED INTERACTION FUNCTIONS   *
  /***************************************/

  /** Commands the robot to read text using Text-To-Speech */
  talk : function (speech, callback) {
    if (this.talkCallback != undefined){
      this.talkCallback();
    }

    this.talkCallback = callback;
    var message = JSON.stringify({
        "name": "TALK",
        "parameters": {
            text: speech
        },
        "id": this.commandid
    });
    this.sendMessage(message);

  },//ENDOF talk


  setLedColor: function (led,color) {
    var message = JSON.stringify({
        "name": "SET-LEDCOLOR",
        "parameters": {
            led:led,
            color:color
        },
        "id": this.commandid
    });
    this.sendMessage(message);
    //END OF CHANGECOLOR FUNCTION
  },


  /** Commands the robot to play a musical note */
  playNote : function (index, time) {
    var message = JSON.stringify({
        "name": "PLAY-NOTE",
        "parameters": {
            index:index,
            time:time
        },
        "id": this.commandid
    });
    this.sendMessage(message);

  },//ENDOF playNote


  /** Returns the last musical note detected by the robot */
  getLastNote : function(){
    return this.statusmap.get("lastNote");
  },//ENDOF getLastNote

    /** Returns the duration of the last musical note detected by the robot */
    getLastNoteDuration : function(){
      return this.statusmap.get("lastNoteDuration");
    },//ENDOF getLastNoteDuration

  processClapStatus : function() {

    claps = this.statusmap.get("claps");
    if (claps == null) claps = 0;
    claps++;

    this.statusmap.set("claps", claps);    

    this.callCallback("onNewClap");

  },

  getClaps : function() {
    return this.statusmap.get("claps");
  },
  

  /*********************************************/
  /* ENDOF SOUND-BASED INTERACTION FUNCTIONS   *
  /*********************************************/

  //---------------------------------------

  /***************************************/
  /* SMARTPHONE SENSORS FUNCTIONS        *
  /***************************************/

  /** Returns the current orientation of each axis (yaw, pitch, roll) of the smartphone */
  getOrientation :function(axis) {
    if (axis=="yaw") {
      return this.statusmap.get("yaw");

    }else if (axis=="pitch") {
      return this.statusmap.get("pitch");

    }else{
      return this.statusmap.get("roll");
    }

  },//ENDOF getOrientation


  /** Returns the current accleration of each axis (x, y, z) of the smartphone */
  getAcceleration :function(axis) {
    if (axis=="x") {
      return this.statusmap.get("xaccel");

    }else if (axis=="y") {
      return this.statusmap.get("yaccel");

    }else{
      return this.statusmap.get("zaccel");
    }

  },//ENDOF getAcceleration

  /** Commands the robot to return the last known ambient light value */
  getLightBrightness: function () {
    var message = JSON.stringify({
        "name": "GETBRIGHTNESS",
        "parameters": {},
        "id": this.commandid
    });
    this.sendMessage(message);
  }, //ENDOF getLightBrightness

  /** Returns the last known ambient light value */
  getBrightness : function () {
    return this.statusmap.get("brightness");
  },

  /** Notifies that the ambient light value has changed */
  brightnessChanged: function (callback) {
    if (callback != undefined){
      callback();
    }
  }, //ENDOF brightnessChanged

  checkOboBatt : function () {
    return this.statusmap.get("obobatterylevel");
    //END OF CHECKBATT FUNCTION
  },


  /***************************************/
  /* ENDOF SMARTPHONE SENSORS FUNCTIONS  *
  /***************************************/

  //---------------------------------------

  /***************************************/
  /* VISION-BASED INTERACTION FUNCTIONS   *
  /***************************************/

  /** Activates/deactivates the detection of each of the 4 different color-blobs supported */
  configureBlobDetection: function (red, green, blue, custom) {
    var message = JSON.stringify({
        "name": "CONFIGURE-BLOBTRACKING",
        "parameters": {
            "red":red,
            "green":green,
            "blue":blue,
            "custom":custom
        },
        "id": this.commandid
    });
    this.sendMessage(message);

  },//ENDOF configureBlobDetection


  /** Returns the coords (x or y axis) of the last defected face */
  getFaceCoord :function(axis) {
    if (axis=="x") {
      return this.statusmap.get("facex");

    }else{
      return this.statusmap.get("facey");
    }

  },//ENDOF getFaceCoord

  getBlobCoord : function(color, axis){
    return this.statusmap.get("blobPos"+axis+color);
  },

  getBlobSize : function(color){
    return this.statusmap.get("blobSize"+color);
  },


  /** Returns the estimated distance to last detected face */
  getFaceDist : function () {
    return this.statusmap.get("facedist");
  },//ENDOF getFaceDist

  getQRCoord(axis){
    if (axis=="x") {
      return this.statusmap.get("qrx");

    }else{
      return this.statusmap.get("qry");
    }
  },//ENDOF getQRCoord

  getQRPoint(point){
    return {x:this.statusmap.get("p"+point+"x"),y: this.statusmap.get("p"+point+"y")}
  },//ENDOF getQRpoint

  getQRDist(){
    
      return this.statusmap.get("qrdist");

  },//ENDOF getQRDist

  getQRId(){
    
    return this.statusmap.get("qrid");

},//ENDOF getQRId

  /**********************************************/
  /* ENDOF VISION-BASED INTERACTION FUNCTIONS   *
  /**********************************************/



  //---------------------------------------------

  /**********************************************/
  /* TOUCH-BASED INTERACTION FUNCTIONS          *
  /**********************************************/

  /** Returns the coords (x or y axis) of the last TAP of the user in the screen */
  getTapCoord :function(axis) {
    if (axis=="x") {
      return this.statusmap.get("tapx");

    }else{
      return this.statusmap.get("tapy");
    }

  },//ENDOF getTapCoord


  getTapZone : function() {
    x = this.getTapCoord("x");
    y = this.getTapCoord("y");

    if (x!=null && y!=null) {
      return this.coordsToZone(x, y);
    }
    else {
      return this.coordsToZone(0,0);
    }
  },

  /** Returns the last angle of a fling gesture in the smartphone screen */
  checkFlingAngle : function () {
    return this.statusmap.get("flingangle");
  },//ENDOF checkFlingAngle


  /**********************************************/
  /* ENDOF TOUCH-BASED INTERACTION FUNCTIONS    *
  /**********************************************/


  //---------------------------------------------

  /**********************************************/
  /* UTILITY FUNCTIONS                          *
  /**********************************************/

  /** Commands the robot to not enter in sleep mode*/
  keepAliveMsg : function () {
    var message = JSON.stringify({
        "name": "KEEP-ALIVE",
        "parameters": {},
        "id": this.commandid
    });
    this.sendMessage(message);

  }, //ENDOF keepAliveMsg

  /** Sends a keep alive message if, and only if, have elapsed
   * more than this.maxKeepAlivePeriod millisends since the last
   * keep alive message sent.
   */
  keepAlive : function() {
    newKeepAliveTime = this.timestamp();
    if ((newKeepAliveTime - this.lastKeepAliveTime) > this.maxKeepAlivePeriod) {
      this.lastKeepAliveTime = newKeepAliveTime;
      this.keepAliveMsg();
    }
  }, //ENDOF keepAlive

  changeStatusFrequency : function (freq) {
    var message = JSON.stringify({
        "name": "SET-SENSOR-FREQUENCY",
        "parameters": {"frequency":freq},
        "id": this.commandid
    });
    this.sendMessage(message);

  }, //ENDOF keepAliveMsg

  resetFaceSensor : function() {
    //face sensor
    this.statusmap.set("facex",0);
    this.statusmap.set("facey",0);
    this.statusmap.set("facedist","far");
  },

  resetFlingSensor : function() {
    this.statusmap.set("flingangle",0);
  },

  resetTapSensor : function() {
    this.statusmap.set("tapx",0);
    this.statusmap.set("tapy",0);
  },

  resetOrientationSensor : function() {
    this.statusmap.set("yaw",0);
    this.statusmap.set("pitch",0);
    this.statusmap.set("roll",0);
  },

  resetAccelerationSensor : function() {
    this.statusmap.set("xaccel",0);
    this.statusmap.set("yaccel",0);
    this.statusmap.set("zaccel",0);
  },

  resetIRs : function() {
    this.setIRValue('Back-R',0);
    this.setIRValue('Back-C',0);
    this.setIRValue('Front-RR',0);
    this.setIRValue('Front-R',0);
    this.setIRValue('Front-C',0); 
    this.setIRValue('Front-L',0);
    this.setIRValue('Front-LL',0);
    this.setIRValue('Back-L',0);

  },

  resetBlobSensor : function() {
    this.statusmap.set("blobPosxgreen",0);
    this.statusmap.set("blobPosygreen",0);
    this.statusmap.set("blobSizegreen",0);
    this.statusmap.set("blobPosxred",0);
    this.statusmap.set("blobPosyred",0);
    this.statusmap.set("blobSizered",0);
    this.statusmap.set("blobPosxblue",0);
    this.statusmap.set("blobPosyblue",0);
    this.statusmap.set("blobSizeblue",0);
    this.statusmap.set("blobPosxcustom",0);
    this.statusmap.set("blobPosycustom",0);
    this.statusmap.set("blobSizecustom",0);
  },

  resetQRSensor: function() {
    this.statusmap.set("qrid",'');
    this.statusmap.set("qrx",0);
    this.statusmap.set("qry",0);
    this.statusmap.set("qrdist",0);
    this.statusmap.set("p1x",0);
    this.statusmap.set("p1y",0);
    this.statusmap.set("p2x",0);
    this.statusmap.set("p2y",0);
    this.statusmap.set("p3x",0);
    this.statusmap.set("p3y",0);
  },  

  resetNoteSensor : function() {
    this.statusmap.set("lastNote",0);
  },

  resetClapSensor : function() {
    this.statusmap.set("claps", 0);
  },

  resetSensors : function () {
    this.resetFaceSensor();

    this.resetFlingSensor();

    this.resetTapSensor();

    this.resetOrientationSensor();

    this.resetAccelerationSensor();

    this.resetIRs();

    this.resetBlobSensor();

    this.resetNoteSensor();

    this.resetClapSensor();

    this.resetQRSensor();
  },

  getError : function () {
    return this.statusmap.get("error");
    //END OF GETCOLOR FUNCTION
  },

  timestamp : function() {
    return (new Date()).getTime();
  },

  /** Tranforms TAP coords to "face zones" */
 coordsToZone : function(x, y){
  
    if (y == 0 && x == 0) {
      return "none";
    }else if (y<17){
        return "forehead";
    }else if (this.rangeFun(y,"between",17,56) && this.rangeFun(x,"between", 15, 85)){
        return "eye";
    }else if (this.rangeFun(y,"between",65,77) && this.rangeFun(x,"between", 25, 75)){
        return "mouth";
    }else if (this.rangeFun(x,"between",0,15)){
        return "left";
    }else if (this.rangeFun(x,"between",85,100)){
        return "right";
    }else if (this.rangeFun(y,"between",77,100) && this.rangeFun(x,"between", 15, 85)){
        return "chin";
    }
  },


  /**********************************************/
  /* ENDOF UTILITY FUNCTIONS                    *
  /**********************************************/




  //TODO --> Move to base block or remove?
  getPanPosition : function () {
    return this.statusmap.get("panPos");
    //END OF GETCOLOR FUNCTION
  },

  //TODO --> Move to base block or remove?
  getTiltPosition : function () {
    return this.statusmap.get("tiltPos");
    //END OF GETCOLOR FUNCTION
  },

  callCallback : function(callbackName) {
    
    if (this.callbackmap.get(callbackName) != null) {
      this.callbackmap.get(callbackName)();
    }else{
      console.log('Bad callback call on '+callbackName);
    }
  },


  /******************************/
  /* MESSAGE PROCESSING         *
  /******************************/

  /** Manages the processing of each different status message received from the remote robot */
  manageStatus : function (msg) {


    //console.log(msg.name);
    if (msg.name == "TapNumber"){
      console.log(msg.value);
    }
    if (msg.name == "NEWCOLOR"){
      this.callCallback("onNewColor");
      console.log("NEWCOLOR");
      //console.log(msg.value["color"]);
      this.statusmap.set("color",msg.value["color"]);
      console.log(this.statusmap.get("color"));
    }

    else if (msg.name == "IRS"){
        for (var key in msg.value) {
            this.setIRValue(key,msg.value[key]);
        }
    }


    else if (msg.name == "BAT-BASE") {
      this.statusmap.set("batterylevel",parseInt(msg.value["level"]));
      if (parseInt(msg.value["level"])<20){
        this.callCallback("onLowBatt");
      }
    }

    else if (msg.name == "BAT-PHONE") {
      this.statusmap.set("obobatterylevel",parseInt(msg.value["level"]));
      if (parseInt(msg.value["level"])<20){
        this.callCallback("onLowOboBatt");
      }
    }

    else if (msg.name == "FACE") {
      this.statusmap.set("facex",parseInt(msg.value["coordx"]));
      this.statusmap.set("facey",parseInt(msg.value["coordy"]));
      if (parseInt(msg.value["distance"])==-1){
        this.callCallback("onLostFace");
        this.lostFace = true;        
        this.statusmap.set("facedist","none");
        
      }else{
        if (this.lostFace){
          this.callCallback("onNewFace");
          this.lostFace = false;        
          
        }
        if (parseInt(msg.value["distance"])>45){
          this.statusmap.set("facedist","close");
        }else if (parseInt(msg.value["distance"])<25){
          this.statusmap.set("facedist","far");
        } else {
          this.statusmap.set("facedist","mid");
        }
      }


    }

    else if (msg.name == "NEWFACE") {
      this.statusmap.set("facex",parseInt(msg.value["coordx"]));
      this.statusmap.set("facey",parseInt(msg.value["coordy"]));

      if (parseInt(msg.value["distance"])>45){
        this.statusmap.set("facedist","close");
      }else if (parseInt(msg.value["distance"])<25){
        this.statusmap.set("facedist","far");
      } else {
        this.statusmap.set("facedist","mid");
      }


    }
    else if (msg.name == "FOUNDFACE") {
      //console.log("FOUNDFACE");
      this.callCallback("onNewFace");
    }

    else if (msg.name == "LOSTFACE") {
      //console.log("LOSTFACE");
      this.callCallback("onLostFace");
    }


    else if (msg.name == "FALLSTATUS"){
      //console.log(msg);
      for (var key in msg.value) {
        //console.log(key);
          this.statusmap.set(key,(msg.value[key] == "true"));
          if(this.statusmap.get(key)){
            //console.log("OnFall");
            if (!!this.callbackmap.get("onFall")){
            (this.callbackmap.get("onFall"))(key);
            }
          }
      }
    }

    else if (msg.name == "GAPSTATUS"){
      //console.log(msg);
      for (var key in msg.value) {
        //console.log(key+" "+msg.value[key]+" "+(msg.value[key] == "true"));
          this.statusmap.set(key,(msg.value[key] == "true"));
          if((this.statusmap.get(key))){
            //console.log("OnGap");
            if(!!this.callbackmap.get("onGap")){
            (this.callbackmap.get("onGap"))(key);
            }else{
              console.log('Bad callback call on GAPSTATUS');
            }
          }

      }

    }

    else if (msg.name == "TAP") {
      //console.log(msg);
      this.statusmap.set("tapx",parseInt(msg.value["coordx"]));
      this.statusmap.set("tapy",parseInt(msg.value["coordy"]));
      this.callCallback("onNewTap");
    }

    else if (msg.name == "FLING") {

      this.statusmap.set("flingangle",parseInt(msg.value["angle"]));
      this.statusmap.set("flingtime",parseInt(msg.value["time"]));
      this.statusmap.set("flingdistance",parseInt(msg.value["distance"]));

      this.callCallback("onNewFling");
    }

    else if (msg.name == "CLAP") {
      this.processClapStatus();
    }

    else if (msg.name == "AMBIENTLIGHT") {
      this.statusmap.set("brightness",parseInt(msg.value["level"]));

    }

    else if (msg.name == "ORIENTATION") {
      //console.log(msg);

      this.statusmap.set("yaw",parseInt(msg.value["yaw"]));
      this.statusmap.set("pitch",parseInt(msg.value["pitch"]));
      this.statusmap.set("roll",parseInt(msg.value["roll"]));
    }

    else if (msg.name == "ACCELERATION") {
      this.statusmap.set("xaccel",parseFloat(msg.value["xaccel"]));
      this.statusmap.set("yaccel",parseFloat(msg.value["yaccel"]));
      this.statusmap.set("zaccel",parseFloat(msg.value["zaccel"]));

    }

    else if (msg.name == "MEASUREDCOLOR") {
      //console.log(msg);
      this.statusmap.set("colorr",parseInt(msg.value["R"]));
      this.statusmap.set("colorg",parseInt(msg.value["G"]));
      this.statusmap.set("colorb",parseInt(msg.value["B"]));

    }

    else if (msg.name == "DIE") {
      console.log("Die message");
      this.closeConnection(false);
    }

    

    else if (msg.name == "ONERROR") {
      console.log("ERROR "+ msg.value['error']);
      this.statusmap.set("error",msg.value['error']);

      this.callCallback("onError");
    }
    else if (msg.name == "ONPHRASE") {
      //console.log('ONPHRASE '+msg.value['text']);
      if (!!this.callbackmap.get("onPhrase")){
        (this.callbackmap.get("onPhrase"))(msg.value['text']);
      }
    }
    else if (msg.name == "UNLOCK-MOVE") {
      //console.SET-SENSOR-FREQUENCYlog('UNLOCK-MOVE '+msg.value['blockid']);
      //(this.blockingcallbackmap.get(""+msg.value['blockid']))();
      if(!!this.wheelsCallbackMap.get(msg.value['blockid'])){
        this.wheelsCallbackMap.get(msg.value['blockid'])();
        this.wheelsCallbackMap.delete(msg.value['blockid']);
      }else{
        console.log('Bad callback call on UNLOCK-MOVE');
      }
    }
    else if (msg.name == "UNLOCK-TILT") {
      //console.log('UNLOCK-TILT '+msg.value['blockid']);
      //(this.blockingcallbackmap.get(""+msg.value['blockid']))();
      if(!!this.tiltCallbackMap.get(msg.value['blockid'])){
        this.tiltCallbackMap.get(msg.value['blockid'])();
        this.tiltCallbackMap.delete(msg.value['blockid']);
      }else{
        console.log('Bad callback call on UNLOCK-TILT');
      }
    }
    else if (msg.name == "UNLOCK-PAN") {
      //console.log('UNLOCK-PAN '+msg.value['blockid']);
      //(this.blockingcallbackmap.get(""+msg.value['blockid']))();
      if(!!this.panCallbackMap.get(msg.value['blockid'])){
        this.panCallbackMap.get(msg.value['blockid'])();
        this.panCallbackMap.delete(msg.value['blockid']);
      }else{
        console.log('Bad callback call on UNLOCK-PAN');
      }
    }
    else if (msg.name == "UNLOCK-DEGREES") {
      //console.log("UNLOCK-DEGREES"+msg.value['blockid']);
      //(this.blockingcallbackmap.get(""+msg.value['blockid']))();
      if(!!this.wheelsCallbackMap.get(msg.value['blockid'])){
        this.wheelsCallbackMap.get(msg.value['blockid'])();
        this.wheelsCallbackMap.delete(msg.value['blockid']);
      }else{
        console.log('Bad callback call on UNLOCK-DEGREES');
      }
    }
    else if (msg.name == "PAN") {
      //console.log("PAN "+msg.value['panPos']);
      this.statusmap.set("panPos",this.roboboToScratchAngle(parseInt(msg.value['panPos'])));
    }

    else if (msg.name == "TILT") {
      //console.log("TILT "+msg.value['tiltPos']);

      this.statusmap.set("tiltPos",parseInt(msg.value['tiltPos']));
    }
    else if (msg.name == "BLOB") {
      //console.log(msg.value['color']+'  '+msg.value['posx']+'  '+msg.value['posy']+'  '+msg.value['size']);
      this.statusmap.set("blobPosx"+msg.value['color'],msg.value['posx']);
      this.statusmap.set("blobPosy"+msg.value['color'],msg.value['posy']);
      this.statusmap.set("blobSize"+msg.value['color'],msg.value['size']);
      this.callCallback("onNewBlob");

    }

    else if (msg.name == "NOTE") {
      //console.log(msg.value['name']+'  '+msg.value['index']+'  '+msg.value['octave']+'  '+msg.value['duration']);
      this.statusmap.set("lastNote",msg.value['name']);
      this.statusmap.set("lastNoteDuration",msg.value['duration']);
      

      this.callCallback("onNewNote");

    }
    else if (msg.name == "UNLOCK-TALK") {
      console.log("END OF SPEECH");
      if (!!this.talkCallback){
        this.talkCallback();
        this.talkCallback = undefined;
      }

    }
    else if (msg.name == "WHEELS") {
      //console.log("WHEELS "+msg.value['wheelPosL']);

      this.statusmap.set("wheelPosR",parseInt(msg.value['wheelPosR']));
      this.statusmap.set("wheelPosL",parseInt(msg.value['wheelPosL']));
      this.statusmap.set("wheelSpeedR",parseInt(msg.value['wheelSpeedR']));
      this.statusmap.set("wheelSpeedL",parseInt(msg.value['wheelSpeedL']));
    }
    else if (msg.name == "OBSTACLES") {

      /*obstacle = false;

      for (var key in msg.value) {
        this.statusmap.set(key,msg.value[key]);
        if (msg.value[key]=="true"){
          obstacle = true;
        }
      }
      if (obstacle){
        this.callbackmap.get("onObstacle")();
      }
      */
    }
    else if (msg.name == "LED") {
      this.statusmap.set(msg.value['id']+"LED-R",msg.value['R']);
      this.statusmap.set(msg.value['id']+"LED-G",msg.value['G']);
      this.statusmap.set(msg.value['id']+"LED-B",msg.value['B']);

    }
    else if (msg.name == "EMOTION") {
      this.statusmap.set("emotion",msg.value['emotion']);


    }

    else if (msg.name == "QRCODE") {
      //console.log("QR");
      this.statusmap.set("qrx",parseInt(msg.value["coordx"]));
      this.statusmap.set("qry",parseInt(msg.value["coordy"]));
      this.statusmap.set("qrdist",parseInt(msg.value["distance"]));
      this.statusmap.set("p1x",parseInt(msg.value["p1x"]));
      this.statusmap.set("p1y",parseInt(msg.value["p1y"]));
      this.statusmap.set("p2x",parseInt(msg.value["p2x"]));
      this.statusmap.set("p2y",parseInt(msg.value["p2y"]));
      this.statusmap.set("p3x",parseInt(msg.value["p3x"]));
      this.statusmap.set("p3y",parseInt(msg.value["p3y"]));

      this.statusmap.set("qrid",msg.value["id"]);
      this.callbackmap.get("onQR")();
  
    }

    else if (msg.name == "QRCODEAPPEAR") {
      //console.log("NewQR");
      console.log(msg.value)
      this.statusmap.set("qrx",parseInt(msg.value["coordx"]));
      this.statusmap.set("qry",parseInt(msg.value["coordy"]));
      this.statusmap.set("qrdist",parseInt(msg.value["distance"]));
      this.statusmap.set("p1x",parseInt(msg.value["p1x"]));
      this.statusmap.set("p1y",parseInt(msg.value["p1y"]));
      this.statusmap.set("p2x",parseInt(msg.value["p2x"]));
      this.statusmap.set("p2y",parseInt(msg.value["p2y"]));
      this.statusmap.set("p3x",parseInt(msg.value["p3x"]));
      this.statusmap.set("p3y",parseInt(msg.value["p3y"]));

      this.statusmap.set("qrid",msg.value["id"]);
      this.callbackmap.get("onQRAppear")();

  
    }

    else if (msg.name == "QRCODELOST") {
      //console.log("LostQR");
      this.statusmap.set("qrx",0);
      this.statusmap.set("qry",0);
      this.statusmap.set("qrdist",0);
      this.statusmap.set("p1x",0);
      this.statusmap.set("p1y",0);
      this.statusmap.set("p2x",0);
      this.statusmap.set("p2y",0);
      this.statusmap.set("p3x",0);
      this.statusmap.set("p3y",0);
      this.statusmap.set("qrid",'');        

      this.callbackmap.get("onQRDisappear")();
    }

    else {
      console.log('Lost status '+ msg.name);
    }
    //console.log('Status '+ msg.name);

  }, //ENDOF manageStatus


  /** Manages the processing of each response message received from the remote robot */
  manageResponse : function (msg) {
      console.log(JSON.stringify(msg));

  }, //ENDOF manageResponse
   
  scratchToRoboboAngle : function(angle){
    return angle +180;
  },

  roboboToScratchAngle: function(angle){
    return angle -180;
  },

  rangeFun: function(input,type,r1,r2) {		
    	
    if (type == "between"){		
      if(r1<r2){		
        if ((input>r1)&&(input<r2)){		
          return true;		
        }else {		
          return false;		
        }		
      }else {		
        if ((input>r2)&&(input<r1)){		
          return true;		
        }else {		
          return false;		
        }		
      }		
    }else {		
      if(r1<r2){		
        if ((input<r1)||(input>r2)){		
          return true;		
        }else {		
          return false;		
        }		
      }else {		
        if ((input<r2)||(input>r1)){		
          return true;		
        }else {		
          return false;		
        }		
      }		
    }		
  },
}
// module.exports = Remote;