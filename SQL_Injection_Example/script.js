

function login() {

  //get the user's values
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  
  //build a new SQL string
  var sql = "SELECT * FROM Users WHERE Username = '" + username + "' AND Password = '" + password + "';";
  
  //display it
  document.getElementById("sql_example").innerHTML = sql;

  //cleanup
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
}



window.addEventListener("load", (event) => {
  const el = document.getElementById("login");
  el.addEventListener("click", login, false);
});