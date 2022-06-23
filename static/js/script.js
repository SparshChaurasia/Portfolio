function removePopup() {
    const popup = document.getElementsByClassName("popup__container")
    let lastElement = popup[popup.length -1]
    
    lastElement.remove()
}