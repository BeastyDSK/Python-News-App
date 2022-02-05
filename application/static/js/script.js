const newsCards = document.querySelector(".news-cards");
const searchItem = document.querySelector("#searchItem");
const searchBtn = document.querySelector("#searchBtn");

// Handling the form submit event. Calls getData method if searchString is valid.
searchBtn.addEventListener("click", (e) => {
    e.preventDefault();
    let searchString = String(searchItem.value);
    if (searchString && searchString.trim().length > 0) {
        getData(searchString);
    } else {
        alert("No data provided to get the News Feed...");
    }
});

// Checking if the data is present for the given search data. If yes the data will be updated else it will alert the user.
function getData(searchString) {
    fetch(`/search=${searchString}`)
        .then((searchData) => searchData.text())
        .then((d) => {
            if (d.trim().length > 0) newsCards.innerHTML = d;
            else alert("Data not found for the given search result.");
        });
}
