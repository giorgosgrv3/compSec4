rule detect_pwned {
    meta:
        description = "detect bad code inside channel.py"
    strings:
        $a = "pwned"
	$b = "PWNED"

    condition:
        $a or $b
}
