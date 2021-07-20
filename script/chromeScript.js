// ==UserScript==
// @name         HackTools
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  extension chrome du logiciel Hacktools qui permet de gerer les fenetres !
// @author       Toutpuissantged
// @match        http://sobricom.net/success.html
// @icon         https://www.google.com/s2/favicons?domain=sobricom.net
// @grant        none
// ==/UserScript==

(function() {
    const url = window.location.hostname
    const hacked_url = 'sobricom.net'
    console.log(url)
    function closeWindow(){
        window.close()
        console.log('time is out')
    }
    if(url===hacked_url){
        setTimeout(closeWindow(),5000)
    }
    console
    // Your code here...
})();