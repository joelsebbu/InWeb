console.log('hello world');
// for ripple button
import {MDCRipple} from '@material/ripple/index';
const ripple = new MDCRipple(document.querySelector('.submit-button'));

//for radio button
import {MDCFormField} from '@material/form-field';
import {MDCRadio} from '@material/radio';

const radio = new MDCRadio(document.querySelector('.mdc-radio'));
const formField = new MDCFormField(document.querySelector('.mdc-form-field'));
formField.input = radio;


//for text field
// import {MDCTextField} from '@material/textfield';
// const textField = new MDCTextField(document.querySelector('.mdc-text-field'));

//for app bar
import {MDCTopAppBar} from '@material/top-app-bar';

// Instantiation
const topAppBarElement = document.querySelector('.mdc-top-app-bar');
const topAppBar = new MDCTopAppBar(topAppBarElement);

//Icon Button
// import {MDCRipple} from '@material/ripple';

const iconButtonRipple = new MDCRipple(document.querySelector('.mdc-icon-button'));
iconButtonRipple.unbounded = true;

import {MDCCheckbox} from '@material/checkbox';

const checkbox = new MDCCheckbox(document.querySelector('.mdc-checkbox'));
formField.input = checkbox;

import {MDCDataTable} from '@material/data-table';
const dataTable = new MDCDataTable(document.querySelector('.mdc-data-table'));