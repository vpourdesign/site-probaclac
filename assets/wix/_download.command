#!/bin/bash
# Telecharge tous les medias wix referencees par les pages Probaclac site-2026
# vers ce dossier (assets/wix/). Genere automatiquement par Cowork.
cd "$(dirname "$0")" || exit 1
echo "Telechargement des medias Probaclac vers: $(pwd)"
ITEMS=( \
  "https://static.wixstatic.com/media/11062b_3da4a26484194105bde5b3935f5afb7bf000.jpg|11062b_3da4a26484194105bde5b3935f5afb7bf000.jpg" \
  "https://static.wixstatic.com/media/623234_003a4f9d94b7496e82593972ec848e22~mv2.png|623234_003a4f9d94b7496e82593972ec848e22.png" \
  "https://static.wixstatic.com/media/623234_1401e0501d8b4cdf8951d0e73669c094~mv2.png|623234_1401e0501d8b4cdf8951d0e73669c094.png" \
  "https://static.wixstatic.com/media/623234_2ca0d945baef427a8209750499a737f9~mv2.png|623234_2ca0d945baef427a8209750499a737f9.png" \
  "https://static.wixstatic.com/media/623234_2dba2af8e279412ca7d01fd0a9a81aaf~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_2dba2af8e279412ca7d01fd0a9a81aaf.jpg" \
  "https://static.wixstatic.com/media/623234_31f03188e94c40d5b213b432ad847171~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_31f03188e94c40d5b213b432ad847171.jpg" \
  "https://static.wixstatic.com/media/623234_374bd5e1040340aaa42a306b1ab168ef~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_374bd5e1040340aaa42a306b1ab168ef.jpg" \
  "https://static.wixstatic.com/media/623234_3c64e30ea6294c0091be12b94743e304~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_3c64e30ea6294c0091be12b94743e304.jpg" \
  "https://static.wixstatic.com/media/623234_3f4f653f708d4a38879c16ecb35f8292~mv2.jpg|623234_3f4f653f708d4a38879c16ecb35f8292.jpg" \
  "https://static.wixstatic.com/media/623234_449a15e9fb3b4971a31217576162a682~mv2.png|623234_449a15e9fb3b4971a31217576162a682.png" \
  "https://static.wixstatic.com/media/623234_53e748d26b8b436bb231214e53d3f455~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_53e748d26b8b436bb231214e53d3f455.jpg" \
  "https://static.wixstatic.com/media/623234_575184a3ab2a49368ed244327cc5207b~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_575184a3ab2a49368ed244327cc5207b.jpg" \
  "https://static.wixstatic.com/media/623234_6f5f97bceff741be949e264710ccc5b8~mv2.png|623234_6f5f97bceff741be949e264710ccc5b8.png" \
  "https://static.wixstatic.com/media/623234_82219e3c86ae48d9954baac0210d9aaf~mv2.jpg|623234_82219e3c86ae48d9954baac0210d9aaf.jpg" \
  "https://static.wixstatic.com/media/623234_83be60d2f5084fc38ff5429c6d4be9ac~mv2.png|623234_83be60d2f5084fc38ff5429c6d4be9ac.png" \
  "https://static.wixstatic.com/media/623234_85b873c9680949899a17031b4d5104c6~mv2.png|623234_85b873c9680949899a17031b4d5104c6.png" \
  "https://static.wixstatic.com/media/623234_8966fbc38d77481bb5d85d60283af9ee~mv2.png|623234_8966fbc38d77481bb5d85d60283af9ee.png" \
  "https://static.wixstatic.com/media/623234_9f990f1bc9534aa4aea99a4b0d9809d8~mv2.png|623234_9f990f1bc9534aa4aea99a4b0d9809d8.png" \
  "https://static.wixstatic.com/media/623234_a069aaba10fc4cc2a0555f996d3cdf90~mv2.jpg|623234_a069aaba10fc4cc2a0555f996d3cdf90.jpg" \
  "https://static.wixstatic.com/media/623234_b46b34c9f86a4c35b9708671406e569e~mv2.png|623234_b46b34c9f86a4c35b9708671406e569e.png" \
  "https://static.wixstatic.com/media/623234_b85c1ce4f42b4f7f875d9fd9d6f55c5b~mv2.png|623234_b85c1ce4f42b4f7f875d9fd9d6f55c5b.png" \
  "https://static.wixstatic.com/media/623234_d1e3a4f56c7e4013b560d97c6b54d607~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_d1e3a4f56c7e4013b560d97c6b54d607.jpg" \
  "https://static.wixstatic.com/media/623234_d7b0658893914abc9ae5d5275c0c2f41~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_d7b0658893914abc9ae5d5275c0c2f41.jpg" \
  "https://static.wixstatic.com/media/623234_e34e7d51c0b045f892556e4a17c1713d~mv2.jpg|623234_e34e7d51c0b045f892556e4a17c1713d.jpg" \
  "https://static.wixstatic.com/media/623234_f5c63088066d4f92b27cf3aa2e65e228~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_f5c63088066d4f92b27cf3aa2e65e228.jpg" \
  "https://static.wixstatic.com/media/623234_f7d1e9ca8c64485f892c5d6f45d3fabb~mv2.jpg/v1/fill/w_900,h_900,al_c,q_85,enc_avif,quality_auto/p.jpg|623234_f7d1e9ca8c64485f892c5d6f45d3fabb.jpg" \
  "https://video.wixstatic.com/video/11062b_3da4a26484194105bde5b3935f5afb7b/1080p/mp4/file.mp4|vid-11062b_3da4a26484194105bde5b3935f5afb7b.mp4" )
ok=0; fail=0
for it in "${ITEMS[@]}"; do
  url="${it%%|*}"; name="${it##*|}"
  if curl -fsSL -A "Mozilla/5.0" "$url" -o "$name"; then
    sz=$(stat -f%z "$name" 2>/dev/null || stat -c%s "$name" 2>/dev/null)
    echo "  OK   $name ($sz o)"; ok=$((ok+1))
  else
    echo "  FAIL $name  <- $url"; fail=$((fail+1))
  fi
done
echo ""
echo "Termine: $ok telecharges, $fail echecs."
echo "Vous pouvez fermer cette fenetre."
