<?php
include "../class/personne.php";
class modelePersonne{
    private $db;
    public function __construct(PDO $_db){
        $this->db = $_db;
    }

    public function getPersonnes(){
        try{
            $reponse = $this->db->prepare("SELECT * FROM personne");
            $reponse->execute();
            $personnes = [];
            while($row = $reponse->fetch(PDO::FETCH_ASSOC)){
                $personnes[] = new Personne($row["nom"],$row["prenom"],$row["age"],$row["adresse"]);
               
            }
            return $personnes;

        }catch(PDOException $e){
            echo "Erreur : ". $e->getMessage();
    
    }
}
}

?>