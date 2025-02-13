let nome= [];      //    function cadastrar()    



function calcular(sinal){
                    document.getElementById("result").innerHTML = "";
                    const n1 = document.getElementById('n1').value;
                    const n2 = document.getElementById('n2').value;
                    let Resultado;
                   

                        switch(sinal){
                            case '+': Resultado = somar(n1,n2);      break;
                            case '-': Resultado = Subtrair(n1,n2);   break;
                            case '*': Resultado = Multiplicar(n1,n2);break;
                            case '/': Resultado = Dividir(n1,n2);    break;
                        }

                        
                        if( Resultado == -1){ document.getElementById("result").innerHTML = "Não se divide por zero!"} else { let ResultadoMultiplicacao = document.getElementById("result").innerHTML = "Resultado: " + Resultado;}

                        function somar(n1,n2){
                            return Number(n1) + Number(n2);
                       }
                       function Dividir(n1,n2){
                           if( n2 == 0 ){ return -1 }else{ return Number(n1) / Number(n2);}
                       }
                       function Subtrair(n1,n2){
                           return (Number(n1) - Number(n2));
                       }               
                       function Multiplicar(n1,n2  ){
                           return(Number(n1)*Number(n2));
                       }

}
function media(){
                    document.getElementById("Mediaresult").innerHTML = "";
                    document.getElementById("Mediaresult2").innerHTML ="";
                    let nome = document.getElementById("nome").value;
                    let n1 = document.getElementById("m1").value;
                    let n2 = document.getElementById("m2").value;
                    let n3 = document.getElementById("m3").value;
                    let med = (Number(n1) + Number(n2) + Number(n3)) / 3;
                    

                        if( med >= 7 ){
                            document.getElementById("Mediaresult").innerHTML =nome +  " foi Aprovado!";
                        }else if( med < 7 && med != 0){
                            document.getElementById("Mediaresult2").innerHTML = nome + " foi Reprovado!";
                            
                        }
                       // -> Todo esse IF/ELSE acima pode ser reescrito como:                                                     
                   // med > 7  ? document.getElementById("Mediaresult").innerHTML =nome +  " foi Aprovado!" : document.getElementById("Mediaresult2").innerHTML = nome + " foi Reprovado!";
                    
}
                
function cadastrar(){
                    let TotClientes = Number(prompt("Quantos clientes serão cadastrados: "));
                    for(let i = 1; i <= TotClientes; i++ ){
                   nome.push( prompt("Digite o nome: "));
                   nome.push(Number(prompt("Digite a idade: ")));
                    } console.table(nome);
                    nome[1] != null ? document.getElementById("cliente").innerHTML = "Ultimo Cadastro : Nome: " + nome[0] + "  |    |  "  + "Idade: " + nome[1] : document.getElementById("cliente").innerHTML = "";
}
function remover(){
                       nome.shift();nome.shift();
                       nome[1]>0 ? document.getElementById("cliente").innerHTML = "Ultimo Cadastro : Nome: " + nome[0] + "  |    |  "  + "Idade: " + nome[1] : document.getElementById("cliente").innerHTML = "";
}
function fatorial (x){
    if(x == 0){return 1;}   else{
        console.log(x + "!")
        return x * fatorial(x-1) ;
        
    }
}
console.log(fatorial(5));
   
                   
 