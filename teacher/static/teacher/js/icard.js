window.onload = function () {
    document.querySelector(".download")
        .addEventListener("click", () => {
            const invoice = document.querySelector(".main_card");
            console.log(invoice);
            console.log(window);
            var opt = {
                margin: 1,
                filename: 'icard.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'landscape' }
            };
            html2pdf().from(invoice).set(opt).save();
        })
}