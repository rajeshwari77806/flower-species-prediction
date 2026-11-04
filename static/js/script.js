document.addEventListener("DOMContentLoaded", function () {

    const card = document.querySelector(".card");

    if (card) {

        card.addEventListener("mousemove", function (event) {

            const rect = card.getBoundingClientRect();

            const x =
                event.clientX - rect.left;

            const y =
                event.clientY - rect.top;

            const centerX =
                rect.width / 2;

            const centerY =
                rect.height / 2;

            const rotateX =
                (y - centerY) / 30;

            const rotateY =
                (centerX - x) / 30;

            card.style.transform =
                `perspective(1000px)
                 rotateX(${rotateX}deg)
                 rotateY(${rotateY}deg)
                 translateY(-5px)`;
        });


        card.addEventListener("mouseleave", function () {

            card.style.transform =
                "perspective(1000px) rotateX(0deg) rotateY(0deg)";

        });

    }


    const inputs =
        document.querySelectorAll("input");


    inputs.forEach(function (input) {

        input.addEventListener("input", function () {

            if (parseFloat(input.value) < 0) {

                input.value = "";

            }

        });

    });

});
