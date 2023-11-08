/**
 * @param {HTMLTableElement} 
 * @param {number}
 * @param {boolean}
 * 
 
*/
function sortTableByColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    //sort whether asc or descending
    const tBody = table.tBodies[0];
    //only works with a single tbody element in the html
    const rows = Array.from(tBody.querySelectorAll("tr"));

    //sort rows
    const sortRows = rows.sort((a, b) => {
        //a and b represent a single table row element
        //grab each ones text content at specified column index
       const aColumnText = a.querySelector(`td:nth-child(${column + 1} )`).textContent.trim();
       const bColumnText = b.querySelector(`td:nth-child(${column + 1} )`).textContent.trim();

      
       return aColumnText > bColumnText ? (-1 * dirModifier) : (1 * dirModifier);

    });
//remove all existing trs from the table
while (tBody.firstChild) {
    tBody.removeChild(tBody.firstChild);
    //while there is a first child then we iterate and remove each one

}

//readd the newly sorted rows
tBody.append(...sortRows);

// remember how the column is currently sorted

table.querySelectorAll('th').forEach(th => th.classList.remove("th-sort-asc", "th-sort-desc"));
table.querySelector(`th:nth-child(${column + 1})`).classList.toggle('th-sort-asc', asc);
table.querySelector(`th:nth-child(${column + 1})`).classList.toggle('th-sort-desc', !asc);
//if we pass in ascending then we add the the new class to the header
//clear out current sorting that may have previously been

}

sortTableByColumn(document.querySelector('table'), 1);

document.querySelectorAll(".table-sortable th").forEach(headerCell => {
    headerCell.addEventListener("click", () => {
        //it needs to go up the parent to the table cell
        const tableElement = headerCell.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(headerCell.parentElement.children, headerCell);
        // calling array function on each child element in the header
        //we are saying find the index of the header cell.
        
        const currentIsAscending = headerCell.classList.contains("th-sort-asc");

        sortTableByColumn(tableElement, headerIndex, !currentIsAscending)

    });
});
