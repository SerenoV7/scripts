// ==UserScript==
// @name         nsw2u.com Anti-AdBlock Remover
// @namespace    https://sereno.pages.dev/
// @version      1.0
// @description  Removes the html element that blocks and contains the Anti ADBlock
// @author       Sereno
// @match        https://nsw2u.com/*
// @match        https://nsw2u.org/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nsw2u.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const h4Element = document.querySelector('h4.adblock_title'); //Selects the "AdBlock Detected" text
    const topDiv = h4Element.parentNode.parentNode.parentNode.parentNode.parentNode; //Selects the top most div that composes the block
    topDiv.parentNode.removeChild(topDiv); //Deletes the block

})();
