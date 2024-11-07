<?php
include "../models/modelePersonne.php";
class ControllerPersonne{
    private $model;
    public function __construct($m){
        $this->model = $m;
    }
    public function getPersonnes(){
       return $this->model->getPersonnes();
        
    }
}

$servername = "localhost";
$username = "root";
$mdp="";
try{
    $connexion = new PDO("mysql:host=$servername;dbname=mvc", $username, $mdp);
    $model = new modelePersonne($connexion);
    $controller = new ControllerPersonne($model);

    $personnes = $controller->getPersonnes();
   include "../views/vuePersonne.php";
}

catch(PDOException $e){
    echo "Erreur : ". $e->getMessage();
}


?>