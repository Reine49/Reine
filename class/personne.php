<?php
class Personne{
    private $nom;
    private $prenom;
    private $age;
    private $adresse;
    public function __construct($n,$p,$a,$ad){
        $this->nom = $n;
        $this->prenom = $p;
        $this->age = $a;
        $this->adresse = $ad;
    }

    public function getNom(){
        return $this->nom;
    }
    public function getPrenom(){
        return $this->prenom;
    }
    public function getAge(){
        return $this->age;
    }
    public function getAdresse(){
        return $this->adresse;
    }
    public function setNom($n){
        $this->nom = $n;
    }

}



?>