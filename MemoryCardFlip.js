function revealAndFadeCards(index = 0) {
  if (index >= cards.length) {
    complete = 16;
    result();
    return;
  }

  cards[index].childNodes[0].style.display = "block";
  cards[index].childNodes[1].style.display = "none";

  cards[index].style.animation = "opa 500ms ease forwards";

  setTimeout(() => {
    revealAndFadeCards(index + 1);
  }, 10);
}

revealAndFadeCards();
clearInterval(counterHandle); 