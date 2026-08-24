try {
    $r = Invoke-WebRequest "http://127.0.0.1:8188/object_info/Image%20Remove%20Background%20(rembg)" -UseBasicParsing -TimeoutSec 10
    $r.Content | Out-File -FilePath "C:\Users\jwu40\Documents\trae_projects\Dakangtu\output\rembg_info.json" -Encoding utf8
    Write-Host "OK len=$($r.Content.Length)"
} catch {
    Write-Host "ERR: $_"
}
