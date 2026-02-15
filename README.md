# my-skills

my 个人技能库，包含 PRD 工作流和测试用例生成等工具。

## 安装

可以通过 `my-marketplace` 安装此插件：

```bash
# 1. 添加 marketplace (如果尚未添加)
/plugin marketplace add my-marketplace https://github.com/uvidswqkscr89/my-marketplace.git

# 2. 安装 skills 插件
/plugin install my-skills@my-marketplace
```

或者直接通过 git 仓库安装：

```bash
/plugin install https://github.com/uvidswqkscr89/my-skills.git
```

## 包含的技能 (Skills)

此插件包含以下技能：

### 1. `write-prd`
用于生成和优化 PRD (产品需求文档) 的工作流。

### 2. `test-case-generation`
用于根据需求自动生成测试用例的工具。

## 开发与贡献

1. 克隆仓库:
   ```bash
   git clone https://github.com/uvidswqkscr89/my-skills.git
   ```
2. 修改或添加技能到 `skills/` 目录。
3. 提交更改。