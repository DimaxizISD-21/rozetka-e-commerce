// price range config

let inputLeft = document.getElementById("input-left");
let inputRight = document.getElementById("input-right");
let range = document.querySelector(".slider > .range");
let priceFrom = document.querySelector(".min");
let priceTo = document.querySelector(".max");

function setLeftValue() {
  let _this = inputLeft,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

  _this.value = Math.min(
    parseInt(_this.value),
    parseInt(inputRight.value) - 10
  );
  priceFrom.textContent = `${_this.value} грн`;

  let percent = ((_this.value - min) / (max - min)) * 100;

  range.style.left = percent + "%";
}

setLeftValue();

function setRightValue() {
  let _this = inputRight,
    min = parseInt(_this.min),
    max = parseInt(_this.max);

  _this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value));
  priceTo.textContent = `${_this.value} грн`;

  let percent = ((_this.value - min) / (max - min)) * 100;

  range.style.right = 100 - percent + "%";
}

setRightValue();

inputLeft.addEventListener("input", setLeftValue);
inputRight.addEventListener("input", setRightValue);

inputLeft.addEventListener("mouseover", (e) => {
  inputLeft.classList.add("hover");
});
inputLeft.addEventListener("mouseout", (e) => {
  inputLeft.classList.remove("hover");
});
inputLeft.addEventListener("mousedown", (e) => {
  inputLeft.classList.add("active");
});
inputLeft.addEventListener("mouseup", (e) => {
  inputLeft.classList.remove("active");
});
inputLeft.addEventListener("touchstart", (e) => {
  inputLeft.classList.add("active");
});
inputLeft.addEventListener("touchend", (e) => {
  inputLeft.classList.remove("active");
});

inputRight.addEventListener("mouseover", (e) => {
  inputRight.classList.add("hover");
});
inputRight.addEventListener("mouseout", (e) => {
  inputRight.classList.remove("hover");
});
inputRight.addEventListener("mousedown", (e) => {
  inputRight.classList.add("active");
});
inputRight.addEventListener("mouseup", (e) => {
  inputRight.classList.remove("active");
});
inputRight.addEventListener("touchstart", (e) => {
  inputRight.classList.add("active");
});
inputRight.addEventListener("touchend", (e) => {
  inputRight.classList.remove("active");
});
