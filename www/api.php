<?php

$config = '/home/inox/mbot/mbot.ini';

$conf = @parse_ini_file($config, true);
try {
	$db = new PDO('sqlite:' . $conf['main']['db']);
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
	die($e->getMessage());
}

switch ($_REQUEST['action']) {
	case 'add':
		$res = $db->prepare('insert into awaiting (dateadded,keywords,state) values (?, ?, 0)');
		try {
			$res->execute(array(time(), $_POST['keywords']));
		} catch (PDOException $e) {
			die($e->getMessage());
		}
		print 'OK';
		break;

	case 'get':
		if (!$res = $db->query('select dateadded,keywords,releasename,releasedate,releasepage,state from awaiting order by state,-releasedate')) {
			die('DB error!');
		}
		$result = array();
		while ($row = $res->fetch(PDO::FETCH_ASSOC)) {
			$row['dateAdded'] = date('d.m.Y H:i', $row['dateAdded']);
			if (!empty($row['releaseDate'])) {
				$row['releaseDate'] = date('d.m.Y H:i', $row['releaseDate']);
			}

			if (!empty($row['releasePage']) && $row['state'] == 1) {
				$row['releaseUrl'] = sprintf('<a href="%s">%s</a>', $row['releasePage'], $row['releaseName']);
			}

			if ($row['state'] == 2) {
				preg_match('/(\d{4})-\w+$/', $row['releaseName'], $rem);
				$row['releaseUrl'] = $conf['main']['downWebPath'] . '/' . $rem[1] . '/' . $row['releaseName'] . '/';
			}

			$result[] = $row;
		}
		header('Content-type: application/json');
		print json_encode($result);
		break;
}

$db = null;
