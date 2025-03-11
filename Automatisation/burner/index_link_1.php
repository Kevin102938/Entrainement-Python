<?php

declare(strict_types=1);

/**
* TemplateName: Standard EXT Burner tracking TimeOne (TOG)
*
 * Lien tracké de la version HTML du mail initial vers la landing page (formulaire LMT TOG) en passant par la
 * plateforme PERF de TOG
 * Usage : Toutes les campagnes au rendement
 *
 * /!\ Sur les LP qui ont un formulaire LMT, ces variables de préremplissage ne sont pas les mêmes, car TimeOne
 * n'utilise pas les mêmes noms de variables pour les mêmes champs.
 *
 * Prérequis dans le fichier des paramètres :
 * - $par_tog_tracking = false; // Le tracking coté TOG est actif (true) ou non (false)
 * -> Le tracking TOG sera actif automatiquement si configuré dans kernix au niveau du message
 *
 * Les paramètres de siret et de l'adresse ne sont pas à remontée, car le formulaire TOG LMT comprend de
 * l'autocomplétion sur ces champs dans la plupart des cas.
 *
 * Pour consulter la liste des correspondances entre les valeurs VM et TOG se rendre sur le fichier README.md.
 *
 * @version: Mise à jour le 03/2024
 */

/*FIX2009-11-26*/

include_once $_ENV['PROJECT_DIR'] . '/common/includes/core/includes.php';

/**
 * @var TOGTracking $TOGTracking
 * @var bool $par_tog_tracking
 * @var string $par_domaine
 * @var string $par_src_index
 * @var string $par_nom_domaine_vm
 * @var string $par_operation
 * @var string $par_fichier_page_lp
 * @var string $par_nom_domaine_client
 */
include_once 'parametres.php';

include $_ENV['PROJECT_DIR'] . '/common/includes/core/php_headers.php';
include $_ENV['PROJECT_DIR'] . '/common/includes/tools/ArrayHelper.php';

$_lt = "hp";

// Paramètre pour l'URL de redirection vers notre LP
$link_vm_url = '#' ;
$link_tog_url = $link_vm_url;
$queryParams = [
];

$queryParams = ArrayHelper::prefixKeys('', $queryParams);

// Lien de tracking suivant le contexte
// https://tracking.publicidees.com/clic.php?partid=2&amp;progid=109&amp;promoid=114285&amp;cb=
if ($par_tog_tracking === true) {
    $redirectUrl = $TOGTracking->getTrackingLink($link_tog_url, $queryParams);
} else {
    $redirectUrl = "$link_vm_url?" . http_build_query(array_merge($_GET, $queryParams));
}

header("Location: $redirectUrl");
exit;
