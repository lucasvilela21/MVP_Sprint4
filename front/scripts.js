/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/vinhos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.vinhos.forEach(item => insertList( item.FA, 
                                                item.VA, 
                                                item.CA,
                                                item.RS,
                                                item.CHL,
                                                item.FSD,
                                                item.TSD,
                                                item.DENS,
                                                item.PH,
                                                item.SLP,
                                                item.ALC,
                                                item.QLT,
                                                item.IS_RED
                                              ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/

getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputFA, inputVA, inputCA,
                        inputRS, inputCHL, inputFSD, 
                        inputTSD, inputDENS, inputPH,
                        inpuSLP, inputALC, inputQLT) => {
    
  const formData = new FormData();
  formData.append('FA', inputFA);
  formData.append('VA', inputVA);
  formData.append('CA', inputCA);
  formData.append('RS', inputRS);
  formData.append('CHL', inputCHL);
  formData.append('FSD', inputFSD);
  formData.append('TSD', inputTSD);
  formData.append('DENS', inputDENS);
  formData.append('PH', inputPH);
  formData.append('SLP', inpuSLP);
  formData.append('ALC', inputALC);
  formData.append('QLT', inputQLT);

  let url = 'http://127.0.0.1:5000/vinho';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, quantidade e valor 
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputFA = document.getElementById("newFA").value;
  let inputVA = document.getElementById("newVA").value;
  let inputCA = document.getElementById("newCA").value;
  let inputRS = document.getElementById("newRS").value;
  let inputCHL = document.getElementById("newCHL").value;
  let inputFSD = document.getElementById("newFSD").value;
  let inputTSD = document.getElementById("newTSD").value;
  let inputDENS = document.getElementById("newDENS").value;
  let inputPH = document.getElementById("newPH").value;
  let inputSLP = document.getElementById("newSLP").value;
  let inputALC = document.getElementById("newALC").value;
  let inputQLT = document.getElementById("newQLT").value;

  if (isNaN(inputFA) || isNaN(inputVA) ||  isNaN(inputCA) || isNaN(inputRS) || isNaN(inputCHL) || isNaN(inputFSD) || isNaN(inputTSD) || isNaN(inputDENS) || 
  isNaN(inputPH) || isNaN(inputSLP) || isNaN(inputALC) || isNaN(inputQLT)){
    alert("Esse(s) campo(s) precisam ser números!");
  } 
  else{
    insertList(inputFA, inputVA, inputCA, inputRS, inputCHL, inputFSD, inputTSD, inputDENS, inputPH, inputSLP,inputALC,inputQLT);
    postItem(inputFA, inputVA, inputCA, inputRS, inputCHL, inputFSD, inputTSD, inputDENS, inputPH, inputSLP,inputALC,inputQLT);
    alert("Item adicionado!");
  }
}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (FA, VA, CA, RS, CHL, FSD, TSD, DENS, PH, SLP,ALC,QL, ISRED) => {
  var item = [FA, VA, CA, RS, CHL, FSD, TSD, DENS, PH, SLP,ALC,QL, ISRED];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }
 
  document.getElementById("newFA").value = "";
  document.getElementById("newVA").value = "";
  document.getElementById("newCA").value = "";
  document.getElementById("newRS").value = "";
  document.getElementById("newCHL").value = "";
  document.getElementById("newFSD").value = "";
  document.getElementById("newTSD").value = "";
  document.getElementById("newDENS").value = "";
  document.getElementById("newPH").value = "";
  document.getElementById("newSLP").value = "";
  document.getElementById("newALC").value = "";
  document.getElementById("newQLT").value = "";

}