const COMPANY = "COMPANY"
const COMPANY_COMPLETE = "COMPANY NAME"
$(".company").html(COMPANY);
$(".company-complete").html(COMPANY_COMPLETE);



const NAV_SECTION_1 = "Home"
const NAV_SECTION_2 = "About"
const NAV_SECTION_3 = "Contact"
const NAV_SECTION_4 = "Login"
const NAV_SECTION_5 = "View Users"
const NAV_SECTION_6 = "Logout"
const NAV_SECTION_7 = "Manager"



$("#nav-section1").html(NAV_SECTION_1);
$("#nav-section2").html(NAV_SECTION_2);
$("#nav-section3").html(NAV_SECTION_3);
$("#nav-section4").html(NAV_SECTION_4);
$("#nav-section5").html(NAV_SECTION_5);
$("#nav-section6").html(NAV_SECTION_6);
$("#nav-section7").html(NAV_SECTION_7);




const MENU_BTN = document.querySelector(".menu-btn");
const NAVIGATION = document.querySelector(".navigation");

MENU_BTN.addEventListener("click", () => {
    MENU_BTN.classList.toggle("active");
    NAVIGATION.classList.toggle("active");
});



const COPYRIGHT = "Copyright © Angelita Santos 2022. Todos os direitos reservados."
$("#copyright").html(COPYRIGHT);



var txtHome = "Fusce vitae dui libero. Maecenas id lectus a quam ornare dictum. Aliquam egestas libero at nisi congue hendrerit."
$("#txtHome").html(txtHome);

var txtAbout = "Cras sed pretium dolor. Duis dapibus dictum mauris, at imperdiet arcu consectetur vulputate. Aenean sed gravida urna. Maecenas efficitur neque urna, nec iaculis justo laoreet vel. Mauris porta mattis efficitur. Integer ac quam vitae sapien malesuada maximus at non lectus. Nam blandit. Fusce fermentum dolor felis, eu accumsan neque blandit ac. Fusce porta ante at nibh varius placerat sed vel mauris. Fusce sit amet vehicula tellus. Nullam lectus odio, commodo ac blandit sit amet, mattis ut orci. Sed convallis hendrerit justo a molestie. Etiam. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
$(".txtAbout").html(txtAbout);

var txtPhoto1 = "Curabitur suscipit mauris at velit porta, non tempus nulla pellentesque. Proin consectetur fringilla sem vitae efficitur. Etiam varius laoreet risus at lobortis."
$(".txtPhoto1").html(txtPhoto1);

var txtPhoto2 = "Fermentum dolor felis, eu accumsan neque blandit ac. Fusce porta ante at nibh varius placerat sed vel mauris. Fusce sit amet vehicula tellus."
$(".txtPhoto2").html(txtPhoto2);



$(function () {

    var curSlide = 0;
    var maxSlide = $('.banner-single').length - 1;
    var delay = 3;

    initSlider();
    changeSlide();

    function initSlider() {
        $('.banner-single').hide();
        $('.banner-single').eq(0).show();
    }

    function changeSlide() {
        setInterval(function () {
            $('.banner-single').eq(curSlide).fadeOut(2000);
            curSlide++;
            if (curSlide > maxSlide)
                curSlide = 0;
            $('.banner-single').eq(curSlide).fadeIn(2000);
        }, delay * 1000);
    }

})



$(document).ready(function () {
    $(".sidebar-btn").click(function () {
        $(".wrapper").toggleClass("collapse");
    });
});
