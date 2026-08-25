# Submit 4 scene backgrounds to ComfyUI via /prompt API
# Loads galgame_bg_zimage_anime_template.json, replaces placeholders, posts 4 times.

$ErrorActionPreference = "Stop"
$templatePath = "C:\Users\jwu40\Documents\trae_projects\Dakangtu\workflows\galgame_bg_zimage_anime_template.json"
$comfyHost = "127.0.0.1"
$comfyPort = 8188

# 通用 negative - 抗 3D 写实 + 抗亚洲符号 + 抗所有 lantern + 抗三轮车
$neg = "photorealistic, real photograph, 3d render, person, people, human, character, figure, crowd, vehicle in foreground, three-wheeled vehicle, rickshaw, cargo tricycle, tuk-tuk, delivery scooter, modern smartphone, LED billboard, text, words, letters, alphabet, chinese characters, japanese characters, signs with letters, banners with text, logos, watermarks, signatures, lowres, bad anatomy, worst quality, blurry, modern glass building, skyscraper, neon lights, wooden architecture, traditional chinese wooden building, wooden door, dark tile roof, red lantern, red paper lantern, lantern, hanging lantern, paper lantern, sky lantern, chinese lantern, oriental lantern, exterior chinese style, pagoda, upturned eaves, hanfu, qipao, tea set, porcelain dishes, tableware, chopsticks, bowls on table, plates on table, columns, pillars, roman columns, greek columns, stone columns, portico"

# 4 个场景的 2D anime 强调版 prompt (v5: 删罗马柱+三轮车, 改底商+台阶+长条招牌)
$scenes = @(
    @{
        prefix = "zimage_anime_v5_bg_scene1_restaurant_doorway"
        seed   = 142081
        pos    = "masterpiece, best quality, 2D anime galgame background art style, cel shaded, flat color, soft anime lighting, illustration, close-up night view of a Chinese restaurant ground floor entrance in a residential mixed-use building, October 2009 night, tall wide open glass doorway on the ground floor with several gray stone steps leading up to the entrance, a long horizontal sign band above the doorway (blank, no text, no letters), warm amber interior light spilling from the open doorway onto gray brick pavement in foreground, modest upper floor residential windows above, dark night sky, distant street with blurred red car tail lights bokeh at the edges, no people, no characters, no lanterns, 1920x1080 wallpaper"
    },
    @{
        prefix = "zimage_anime_v5_bg_scene2_private_dining_room"
        seed   = 142082
        pos    = "masterpiece, best quality, 2D anime galgame background art style, cel shaded, flat color, soft anime lighting, illustration, interior of a modern restaurant private dining room, October 2009, dim warm ambient overhead ceiling lighting, moody intimate low-key atmosphere, deep soft shadows, carved wooden privacy screens between tables, large clean empty round table covered with white tablecloth and a red lazy susan, no dishes no tableware on table, small indoor stone bridge and water feature visible in dim background, soft golden light with deep shadows, cozy enclosed private atmosphere, no people, no signs with letters, no text, no characters, no lanterns, 1920x1080 wallpaper"
    },
    @{
        prefix = "zimage_anime_v5_bg_scene3_dining_table_window"
        seed   = 142083
        pos    = "masterpiece, best quality, 2D anime galgame background art style, cel shaded, flat color, soft anime lighting, illustration, interior view of a modern restaurant dining table near window, October 2009 night, dim warm overhead ceiling lighting, moody low-key atmosphere, large clean empty round table with red lazy susan, no dishes no tableware on table, view through restaurant window of urban street with blurred red car tail lights bokeh, simple window frame, soft golden light with deep shadows, cozy private dining atmosphere, no people, no signs with letters, no text, no characters, no lanterns, 1920x1080 wallpaper"
    },
    @{
        prefix = "zimage_anime_v5_bg_scene4_bus_stop"
        seed   = 142084
        pos    = "masterpiece, best quality, 2D anime galgame background art style, cel shaded, flat color, soft anime lighting, illustration, exterior night view of a Beijing city bus stop, October 2009, a tall thin metal pole with a blank rectangular sign board (no text, no letters), dim overhead street lamp casting soft warm pool of light, simple concrete sidewalk, dry autumn night, deep blue night sky, blurred distant city street with red car tail lights bokeh, quiet nostalgic farewell atmosphere, no people, no text, no characters, no lanterns, 1920x1080 wallpaper"
    }
)

# 读取模板
$templateJson = Get-Content $templatePath -Raw -Encoding UTF8

foreach ($scene in $scenes) {
    # 深拷贝模板,替换占位符 (用 .NET String.Replace 字面替换)
    $wf = $templateJson
    $wf = $wf.Replace('PLACEHOLDER_POSITIVE', $scene.pos)
    $wf = $wf.Replace('PLACEHOLDER_NEGATIVE', $neg)
    $wf = $wf.Replace('PLACEHOLDER_PREFIX', $scene.prefix)

    # 改 seed
    $wfObj = $wf | ConvertFrom-Json
    $wfObj.'3'.inputs.seed = $scene.seed
    $body = @{
        prompt     = $wfObj
        client_id  = "zimage_anime_batch"
    } | ConvertTo-Json -Depth 100

    $uri = "http://${comfyHost}:${comfyPort}/prompt"
    try {
        $resp = Invoke-RestMethod -Uri $uri -Method Post -ContentType "application/json" -Body $body
        Write-Host "[OK] $($scene.prefix) -> prompt_id=$($resp.prompt_id)"
    }
    catch {
        Write-Host "[FAIL] $($scene.prefix) -> $_"
    }
    Start-Sleep -Milliseconds 800
}

Write-Host "`nDone. Check ComfyUI queue for 4 jobs."
