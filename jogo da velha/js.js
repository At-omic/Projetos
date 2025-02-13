let VezPlay = 1;
let Quadrado = "";
let x = "";
let ValorSplice;
let Matriz3x3 = [ [0,2,3],
                  [4,5,6], 
                  [7,8,9] ];
//


//console.log();

function check(){

                   
                // ---
                         if(Matriz3x3[0][0] == Matriz3x3[0][1] && Matriz3x3[0][0] == Matriz3x3[0][2]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                    else if(Matriz3x3[1][0] == Matriz3x3[1][1] && Matriz3x3[1][0] == Matriz3x3[1][2]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                    else if(Matriz3x3[2][0] == Matriz3x3[2][1] && Matriz3x3[2][0] == Matriz3x3[2][2]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                /* -
                   -
                   - */ 
                   else if(Matriz3x3[0][0] == Matriz3x3[1][0] && Matriz3x3[0][0] == Matriz3x3[2][0]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                   else if(Matriz3x3[0][1] == Matriz3x3[1][1] && Matriz3x3[0][1] == Matriz3x3[2][1]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}                   
                   else if(Matriz3x3[0][2] == Matriz3x3[1][2] && Matriz3x3[0][2] == Matriz3x3[2][2]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                //x
                   else if(Matriz3x3[0][0] == Matriz3x3[1][1] && Matriz3x3[0][0] == Matriz3x3[2][2]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}
                   else if(Matriz3x3[0][2] == Matriz3x3[1][1] && Matriz3x3[0][0] == Matriz3x3[2][0]){ if (Matriz3x3[0][0]== 1){ alert("X GANHOU!")}else{alert("O GANHOU")}}


}

function Play(x){
                VezPlay == 1 ?  document.getElementById(x).innerHTML = " X " :  document.getElementById(x).innerHTML = " O ";
                ValorSplice = VezPlay;
                VezPlay = VezPlay* (-1); 


}
function marcar(Quadrado){

        switch (Quadrado){
                case '1q': 
                    Play('1q');
                        Matriz3x3[0].splice(0,1, ValorSplice);
                        
                        check();
                break;
                case '2q': 
                     Play('2q');
                        Matriz3x3[0].splice(1,1, ValorSplice);
                        
                        check();
                break;
                case '3q': 
                        Play('3q');
                            Matriz3x3[0].splice(2,1, ValorSplice);
                            
                            check();
                break;
                case '4q': 
                        Play('4q');
                            Matriz3x3[1].splice(0,1, ValorSplice);
                            
                            check();
                break;
                case '5q': 
                     Play('5q');
                        Matriz3x3[1].splice(1,1, ValorSplice);
                        
                        check();
                break;
                case '6q': 
                     Play('6q');
                        Matriz3x3[1].splice(2,1, ValorSplice);
                        
                        check();
                break;
                case '7q': 
                    Play('7q');
                        Matriz3x3[2].splice(0,1, ValorSplice);
                        
                        check();
                break;
                case '8q': 
                    Play('8q');
                        Matriz3x3[2].splice(1,1, ValorSplice);
                        
                        check();
                break;
                case '9q': 
                     Play('9q'); 
                        Matriz3x3[2].splice(2,1, ValorSplice);
                        
                        check();
                break;

        }

}
function limpar(){         for (i=1; i <= 9; i++){  let x= i+'q';   document.getElementById(x).innerHTML = " "; } 
                            Matriz3x3 = [ [0,2,3],
                                          [4,5,6], 
                                          [7,8,9] ]
                                          console.table(Matriz3x3);;
                }

