# 📤 Git Push to Main - 完整指南

## 🎯 當前狀態

- **當前分支**: `fix-from-a199f8f`
- **目標分支**: `main`
- **遠端倉庫**: `https://github.com/aiformula/secret_talk.git`

## 📋 步驟 1: 添加所有變更

```bash
git add .
```

或者只添加特定文件：
```bash
git add ming/custom_story_reader.py
git add ming/run_custom_story.py
git add ming/relationship_main.py
git add my_custom_story.txt
git add *.md
git add *.txt
```

## 📝 步驟 2: 提交變更

```bash
git commit -m "Fix perspective detection for girl view stories"
```

或者更詳細的提交訊息：
```bash
git commit -m "Fix perspective detection logic

- Enhanced detection algorithm with title bonus
- Added smart path resolution
- Improved visual feedback
- Added test_perspective_detection.py
- Fixed girl view story detection (was incorrectly detected as male)
- Added comprehensive documentation in Cantonese"
```

## 🔀 步驟 3: 切換到 main 分支

```bash
git checkout main
```

## 🔀 步驟 4: 合併你的變更

```bash
git merge fix-from-a199f8f
```

## 📤 步驟 5: 推送到遠端

```bash
git push origin main
```

---

## 🚀 快速方法（一次過）

如果你想直接推送當前分支到 main：

```bash
# 1. 添加所有變更
git add .

# 2. 提交
git commit -m "Fix perspective detection for girl view stories"

# 3. 切換到 main
git checkout main

# 4. 合併變更
git merge fix-from-a199f8f

# 5. 推送
git push origin main
```

---

## ⚠️ 注意事項

1. **確保所有變更已保存**
2. **檢查是否有衝突** - 如果 merge 時有衝突，需要先解決
3. **確認遠端倉庫權限** - 確保你有 push 權限

---

## 🔧 如果遇到問題

### 問題 1: Merge 衝突
```bash
# 查看衝突文件
git status

# 解決衝突後
git add .
git commit -m "Resolve merge conflicts"
git push origin main
```

### 問題 2: 遠端有更新
```bash
# 先拉取遠端更新
git pull origin main

# 解決衝突後再推送
git push origin main
```

### 問題 3: 權限問題
確保你有 GitHub 倉庫的寫入權限

---

## ✅ 成功後會見到

```
Enumerating objects: X, done.
Counting objects: 100% (X/X), done.
Delta compression using up to X threads
Compressing objects: 100% (X/X), done.
Writing objects: 100% (X/X), X.XX KiB | X.XX MiB/s, done.
Total X (delta X), reused X (delta X), pack-reused X
To https://github.com/aiformula/secret_talk.git
   abc1234..def5678  main -> main
```

