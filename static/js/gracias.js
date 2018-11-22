
function gracias() {
	window.alert('Gracias por comprar en Shopify')

}

function cambiar() {
	if (document.getElementById("navbarNav").classList.contains("collapse")) {
		document.getElementById("navbarNav").classList.remove("collapse")
		document.getElementById("navbarNav").classList.add("expanded")

	}else{
		document.getElementById("navbarNav").classList.remove("expanded")
		document.getElementById("navbarNav").classList.add("collapse")
	}
}