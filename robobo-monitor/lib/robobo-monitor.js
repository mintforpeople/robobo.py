
/*******************************************************************************
 * Copyright 2017 Mytech Ingenieria Aplicada <http://www.mytechia.com>
 * Copyright 2017 Gervasio Varela <gervasio.varela@mytechia.com>
 * Copyright 2017 Alma Mallo <alma.mallo@mytechia.com>
 * <p>
 * This file is part of Robobo Scratch Extension.
 * <p>
 * Robobo Scratch Extension is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * <p>
 * Robobo Scratch Extension is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * <p>
 * You should have received a copy of the GNU Lesser General Public License
 * along with Robobo Scratch Extension.  If not, see <http://www.gnu.org/licenses/>.
 ******************************************************************************/

/**
 * Support functions to control the Robobo status page and Robobo dynamic views
 */


var faceLost = 0;
var faceNew = 0;

// IR Sensors number
var frontCIR = "Front-C",
    frontLIR = "Front-L",
    frontLLIR = "Front-LL",
    frontRIR = "Front-R",
    frontRRIR = "Front-RR",
    backCIR = "Back-C",
    backLIR = "Back-L",
    backRIR = "Back-R";

// last note received
var lastNote = undefined;

// gauge

var wheelLeftSpeedGauge;
var wheelRightSpeedGauge;

// claps

var clapNotificationCounter = 0;

/* Change color of claps element and  decrement in 1 the notification counter */


function clapNotificationReceived() {
   clapNotificationCounter++;
   clapNotificationUpdate();
}

function clapNotificationUpdate() {
    setClapsCircleColor("#fffc00");
    setTimeout(function() {
        if (clapNotificationCounter == 0) {
          setClapsCircleColor("#c4e8fe");
        }
    }, 300);
    clapNotificationCounter--;
}


function setClapsCircleColor(color) {
  document.getElementById("audio-sensor-claps-svg").setAttribute("fill", color);
}

function pausecomp(ms) {
  ms += new Date().getTime();
  while (new Date() < ms){}
}

/* Creates gauge elements to show the wheels speed */
function createGaugeElements() {
  var opts = {
    angle: 0, // The span of the gauge arc
    lineWidth: 0.08, // The line thickness
    radiusScale: 0.7, // Relative radius
    pointer: {
      length: 0.6, // // Relative to gauge radius
      strokeWidth: 0.05, // The thickness
      color: '#dddddd' // Fill color
    },
    staticLabels: {
      font: "10px Roboto",  // Specifies font
      labels: [-100, 0,100],  // Print labels at these values
      color: "#424242",  // Optional: Label text color
      fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
    staticZones: [
       {strokeStyle: "#8ac2e9", min: -120, max: 0}, // Red from 100 to 130
       {strokeStyle: "#b5d8f1", min: 0, max: 120}, // Yellow
    ],
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#ffffff', //'#6FADCF',   // Colors
    colorStop: '#ffffff', //'#8FC0DA',    // just experiment with them
    strokeColor: '#ffffff',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true     // High resolution support
  };

  var target = document.getElementById('wheel-left-speed-gauge'); // your canvas element
  wheelLeftSpeedGauge = new Gauge(target).setOptions(opts); // create sexy gauge!
  wheelLeftSpeedGauge.setMinValue(-120);  // Prefer setter over gauge.minValue = 0
  wheelLeftSpeedGauge.maxValue = 120; // set max gauge value
  wheelLeftSpeedGauge.animationSpeed = 1; // set animation speed (32 is default value)
  wheelLeftSpeedGauge.setTextField(document.getElementById("wheel-left-speed"));
  wheelLeftSpeedGauge.set(0); // set actual value


  var target2 = document.getElementById('wheel-right-speed-gauge'); // your canvas element
  wheelRightSpeedGauge = new Gauge(target2).setOptions(opts); // create sexy gauge!
  wheelRightSpeedGauge.setMinValue(-120);  // Prefer setter over gauge.minValue = 0
  wheelRightSpeedGauge.maxValue = 120; // set max gauge value
  wheelRightSpeedGauge.animationSpeed = 1; // set animation speed (32 is default value)
  wheelRightSpeedGauge.setTextField(document.getElementById("wheel-right-speed"));
  wheelRightSpeedGauge.set(0); // set actual value
}

function createElements() {
  createGaugeElements();
}

/** Converts undefined in ' ' **/
function replaceUndefined (value) {
  if (value == undefined) {
    return '&nbsp;&nbsp;';
  }else {
    return value;
  }
}

/* Converts a number with many decimals to a fixed number of decimal places
   @param decimals: the number of decimal places
*/
function formatNumber(value, decimals) {
  if (value == undefined) {
    return '&nbsp;&nbsp;';
  }else {
    return parseFloat(value).toFixed(decimals);
  }
}

/** Returns the GapKey string for the specified gap number */
function getGapKey(gapNumber) {
    return "Gap"+gapNumber;
}

/** Changes the visibility of a SVG element */
function setElementVisibility(element, visibility) {
    if(visibility) {
        element.setAttribute("visibility","visible");
    }
    else {
        element.setAttribute("visibility","hidden");
    }
}

/** Sets the HTML content of the specified element */
function setElementHTML(element, html) {
    document.getElementById(element).innerHTML = html;
}

/*
  Sets the value of battery status.
  @param the id of the battery element
*/
function setBatteryLevel(batteryIconId, batteryValueId, statusValue) {
  var battery0 = "&#xf244";
  var battery25 = "&#xf243";
  var battery50 = "&#xf242";
  var battery75 = "&#xf241";
  var battery100 = "&#xf240";

  if (statusValue == undefined) {
    document.getElementById(batteryIconId).classList.add('battery-no-value');
    document.getElementById(batteryIconId).classList.remove('battery-full');
    document.getElementById(batteryIconId).classList.remove('battery-normal');
    document.getElementById(batteryIconId).classList.remove('battery-low');
  }else {
      document.getElementById(batteryIconId).classList.remove('battery-no-value');
      if (statusValue < 50) {
        document.getElementById(batteryIconId).innerHTML=battery25;
        document.getElementById(batteryIconId).classList.remove('battery-full');
        document.getElementById(batteryIconId).classList.remove('battery-normal');
        document.getElementById(batteryIconId).classList.add('battery-low');
      } else
      if (statusValue >= 50 && statusValue<75) {
        document.getElementById(batteryIconId).innerHTML=battery50;
        document.getElementById(batteryIconId).classList.add('battery-full');
        document.getElementById(batteryIconId).classList.remove('battery-low');
        document.getElementById(batteryIconId).classList.remove('battery-normal');
      } else
      if (statusValue >= 75 && statusValue<100) {
        document.getElementById(batteryIconId).innerHTML=battery75;
        document.getElementById(batteryIconId).classList.add('battery-full');
        document.getElementById(batteryIconId).classList.remove('battery-low');
        document.getElementById(batteryIconId).classList.remove('battery-normal');
      } else
      if (statusValue == 100) {
        document.getElementById(batteryIconId).innerHTML=battery100;
        document.getElementById(batteryIconId).classList.add('battery-full');
        document.getElementById(batteryIconId).classList.remove('battery-low');
        document.getElementById(batteryIconId).classList.remove('battery-normal');
      }
  }
  setElementHTML(batteryValueId, replaceUndefined(statusValue));

}

/** Returns all the parameters of an URL */
function getAllUrlParams(url) {

    // get query string from url (optional) or window
    var queryString = url ? url.split('?')[1] : window.location.search.slice(1);

    // we'll store the parameters here
    var obj = {};

    // if query string exists
    if (queryString) {

        // stuff after # is not part of query string, so get rid of it
        queryString = queryString.split('#')[0];

        // split our query string into its component parts
        var arr = queryString.split('&');

        for (var i=0; i<arr.length; i++) {
            // separate the keys and the values
            var a = arr[i].split('=');

            // in case params look like: list[]=thing1&list[]=thing2
            var paramNum = undefined;
            var paramName = a[0].replace(/\[\d*\]/, function(v) {
                paramNum = v.slice(1,-1);
                return '';
            });

            // set parameter value (use 'true' if empty)
            var paramValue = typeof(a[1])==='undefined' ? true : a[1];

            // (optional) keep case consistent
            paramName = paramName.toLowerCase();
            paramValue = paramValue.toLowerCase();

            // if parameter name already exists
            if (obj[paramName]) {
                // convert value to array (if still string)
                if (typeof obj[paramName] === 'string') {
                    obj[paramName] = [obj[paramName]];
                }
                // if no array index number specified...
                if (typeof paramNum === 'undefined') {
                    // put the value on the end of the array
                    obj[paramName].push(paramValue);
                }
                // if array index number specified...
                else {
                    // put the value at that index number
                    obj[paramName][paramNum] = paramValue;
                }
            }
            // if param name doesn't exist yet, set it
            else {
                obj[paramName] = paramValue;
            }
        }
    }

    return obj;
};


    /** Registers all the callbacks supported by the remote library. */
function registerRemoteCallbacks(rem) {

    rem.registerCallback("onNewColor", function() {
        var colorSensor = rem.checkMeasuredColor('red') + ' | ' + rem.checkMeasuredColor('green') + ' | ' + rem.checkMeasuredColor('blue');
        setElementHTML("color-sensor-value", colorSensor);
    });

    rem.registerCallback("onQR", function() {});
    rem.registerCallback("onQRAppear", function() {});
    rem.registerCallback("onQRDisappear", function() {});

    rem.registerCallback("onIrChanged",function() {});
    rem.registerCallback("onNewFace",function() {
        faceNew = 1;
        faceLost = 0;
    });

    rem.registerCallback("onLostFace",function() {
        faceNew = 0;
        faceLost = 1;
//        setElementVisibility(document.getElementById("robobo-face", 0));
    });

    rem.registerCallback("onFall",function() {});
    rem.registerCallback("onGap",function() {});
    rem.registerCallback("onLowBatt",function() {});
    rem.registerCallback("onLowOboBatt",function() {});
    rem.registerCallback("onNewClap",function() {
//        setElementHTML("audio-sensor-claps", replaceUndefined(rem.getClaps()));
       clapNotificationReceived();
    });

    rem.registerCallback("onNewTap", function() {
        var sensorValue = rem.getTapCoord('x') + "," + rem.getTapCoord('y')
        setElementHTML("tap-sensor-value", sensorValue);
        setElementHTML("tap-zone-value", rem.getTapZone());
    });

    rem.registerCallback("onNewFling",function() {
        //update fling angle in robobo emotion face
        var flingAngle = rem.checkFlingAngle();
        //setFlingAngle(flingAngle);
        setElementHTML("fling-sensor-value", rem.checkFlingAngle()+' º');
    });

    rem.registerCallback("onAccelChanged", function() {});

    rem.registerCallback("onObstacle", function() {

        setElementHTML("ir-sensor-distance-front-l", rem.getObstacle());
    });

    rem.registerCallback("onBrightnessChanged", function() {});

    rem.registerCallback("onError", function() {});
    rem.registerCallback("onConnectionChanges", function() {});


    rem.registerCallback("onNewNote", function() {
      if (lastNote != undefined) {
        pianoLastKey = document.getElementById(lastNote);
        if (isWhiteNote(lastNote)) {
          pianoLastKey.classList.remove('key-white-selected');
          pianoLastKey.classList.add('key-white-unselected');
        }else {
          pianoLastKey.classList.remove('key-black-selected');
          pianoLastKey.classList.add('key-black-unselected')
        }
      }

      lastNote = rem.getLastNote();
      pianoKey = document.getElementById(rem.getLastNote());
      if (isWhiteNote(lastNote)) {
        pianoKey.classList.remove('key-white-unselected');
        pianoKey.classList.add('key-white-selected')
      }else {
        pianoKey.classList.remove('key-black-unselected');
        pianoKey.classList.add('key-black-selected');
      }

      //setElementHTML("audio-sensor-music-note", rem.getLastNote());
    });
}


function isWhiteNote(note) {
   return ((note=="C")||(note =="D")||(note =="E")||(note =="F")||(note =="G")||(note =="A")||(note =="B"))
}

/** This function updates sensing data by polling to the remote library.
    It is mean to be called periodically using JS setInverval() */
function updateSensors() {

    //update brightness sensor
    setElementHTML("brightness-sensor-value", replaceUndefined(rem.getBrightness())+ " Lux");

    //update acceleration sensor
    //var accelSensor = rem.getAcceleration('x') + ' | ' + rem.getAcceleration('y') + ' | ' + rem.getAcceleration('z');
    setElementHTML("accel-sensor-x", formatNumber(rem.getAcceleration('x'),3) +' m/s<sup>2</sup>');
    setElementHTML("accel-sensor-y", formatNumber(rem.getAcceleration('y'),3) +' m/s<sup>2</sup>');
    setElementHTML("accel-sensor-z", formatNumber(rem.getAcceleration('z'),3) +' m/s<sup>2</sup>');

    //update orientation sensor
    var orSensor = replaceUndefined(rem.getOrientation('yaw')) + 'º, ' + replaceUndefined(rem.getOrientation('pitch')) + 'º, ' + replaceUndefined(rem.getOrientation('roll'))+"º";
    setElementHTML("orientation-sensor-value", orSensor);

    //update pan-tilt position

    setElementHTML("pan-sensor-value", replaceUndefined(rem.getPan()));
    setElementHTML("tilt-sensor-value", replaceUndefined(rem.getTilt()));

    //update face position
    var faceX = replaceUndefined(rem.getFaceCoord('x'));
    var faceY = replaceUndefined(rem.getFaceCoord('y'));
    var faceDist = replaceUndefined(rem.getFaceDist());
    var value = faceX + ", " + faceY;
    setElementHTML("facepos-sensor-value", value);

    //setFacePosition(faceDist, faceX, faceY);
    setElementHTML("facedist-sensor-value", replaceUndefined(rem.getFaceDist()));

    // update blob sensor values
    setElementHTML("color-sensor-green-x", replaceUndefined(rem.getBlobCoord("green","x")));
    setElementHTML("color-sensor-green-y", replaceUndefined(rem.getBlobCoord("green","y")));
    setElementHTML("color-sensor-green-size", replaceUndefined(rem.getBlobSize("green")));
    setElementHTML("color-sensor-blue-x", replaceUndefined(rem.getBlobCoord("blue","x")));
    setElementHTML("color-sensor-blue-y", replaceUndefined(rem.getBlobCoord("blue","y")));
    setElementHTML("color-sensor-blue-size", replaceUndefined(rem.getBlobSize("blue")));
    setElementHTML("color-sensor-red-x", replaceUndefined(rem.getBlobCoord("red","x")));
    setElementHTML("color-sensor-red-y", replaceUndefined(rem.getBlobCoord("red","y")));
    setElementHTML("color-sensor-red-size", replaceUndefined(rem.getBlobSize("red")));
    setElementHTML("color-sensor-custom-x", replaceUndefined(rem.getBlobCoord("custom","x")));
    setElementHTML("color-sensor-custom-y", replaceUndefined(rem.getBlobCoord("custom","y")));
    setElementHTML("color-sensor-custom-size", replaceUndefined(rem.getBlobSize("custom")));

      // update qr sensor values

    var qrId = replaceUndefined(rem.getQRId());
    if (qrId.length > 25) {
      qrId = qrId.substring(0,24) + '...';
    }

    setElementHTML("qr-sensor-id", qrId);
    setElementHTML("qr-sensor-x", replaceUndefined(rem.getQRCoord("x")));
    setElementHTML("qr-sensor-y", replaceUndefined(rem.getQRCoord("y")));
    setElementHTML("qr-sensor-size", replaceUndefined(rem.getQRDist()));
  

    // update IR sensors raw value
    var errorValue = 65535; // If the sensor is broken, this value is received.
    var irElement = undefined;

    var value = replaceUndefined(rem.getObstacle(frontCIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-front-c');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-front-c", value);

    var value = replaceUndefined(rem.getObstacle(frontLIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-front-l');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-front-l", value);

    var value = replaceUndefined(rem.getObstacle(frontLLIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-front-ll');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-front-ll", value);

    var value = replaceUndefined(rem.getObstacle(frontRIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-front-r');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-front-r", value);

    var value = replaceUndefined(rem.getObstacle(frontRRIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-front-rr');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-front-rr", value);

    var value = replaceUndefined(rem.getObstacle(backCIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-back-c');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-back-c", replaceUndefined(rem.getObstacle(backCIR)));

    var value = replaceUndefined(rem.getObstacle(backRIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-back-r');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-back-r", value);

    var value = replaceUndefined(rem.getObstacle(backLIR));
    if (value == errorValue) {
          value = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
          irElement = document.getElementById('ir-sensor-raw-back-l');
          irElement.classList.add('value-error');
    }
    setElementHTML("ir-sensor-raw-back-l", value);

    //Battery level
    setBatteryLevel("rob-battery-icon", "rob-battery-value", rem.checkBatt());
    setBatteryLevel("obo-battery-icon", "obo-battery-value", rem.checkOboBatt());


    //Wheel level
    setElementHTML("wheel-right-position", replaceUndefined(rem.getWheel("right","position"))+"º");
    setElementHTML("wheel-left-position", replaceUndefined(rem.getWheel("left","position"))+"º");

    //setElementHTML("wheel-right-speed", replaceUndefined(rem.getWheel("right","speed")));

    var leftSpeed = rem.getWheel("left","speed");
    var rightSpeed = rem.getWheel("right","speed");
    //setElementHTML("wheel-left-speed", replaceUndefined(leftSpeed));

    if (leftSpeed != undefined) {
      wheelLeftSpeedGauge.set(leftSpeed); // set actual value
    }
    if (rightSpeed != undefined) {
      wheelRightSpeedGauge.set(rightSpeed);
    }

}
