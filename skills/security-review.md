# Security Review Skill for AI Coding Agents

Use this skill whenever you are asked to review code, create a PR, or make non-trivial changes.

## English Version

### Mandatory Checks
1. **Secrets & Credentials**  
   - Search for hard-coded API keys, tokens, passwords, private keys.  
   - Check `.env*`, config files, and test fixtures.  
   - If any are found → stop and report immediately.

2. **Input Validation**  
   - All external input (user, network, file, CLI) must be validated and sanitized.  
   - Prefer allow-lists over deny-lists.

3. **Authentication & Authorization**  
   - New endpoints or functions that touch sensitive data must check identity and permission.  
   - Do not assume the caller is trusted.

4. **Injection Risks**  
   - SQL, command, template, LDAP, path traversal.  
   - Prefer parameterized queries / safe APIs.

5. **Dependency & Supply Chain**  
   - Prefer well-maintained packages.  
   - Avoid adding heavy or poorly maintained dependencies for small features.

6. **Logging & Error Messages**  
   - Never log secrets or full sensitive payloads.  
   - Error messages should not leak internal details to end users.

### Output Format
When finishing a security review, always produce:

```markdown
## Security Review Summary
- Secrets found: Yes / No (list them if yes)
- High risk issues: ...
- Medium risk issues: ...
- Recommendations: ...
- Residual risk: Low / Medium / High
```

---

## 中文版本

### 强制检查项
1. **密钥与凭证**  
   - 搜索硬编码的 API key、token、密码、私钥。  
   - 检查 `.env*`、配置文件和测试数据。  
   - 一旦发现立即停止并报告。

2. **输入验证**  
   - 所有外部输入（用户、网络、文件、CLI）必须验证并清理。  
   - 优先使用白名单。

3. **认证与授权**  
   - 新接口或涉及敏感数据的函数必须检查身份和权限。  
   - 不要假设调用方是可信的。

4. **注入风险**  
   - SQL、命令、模板、LDAP、路径穿越。  
   - 优先使用参数化查询或安全 API。

5. **依赖与供应链**  
   - 优先选择维护良好的包。  
   - 避免为小功能引入重型或不活跃的依赖。

6. **日志与错误信息**  
   - 永远不要记录密钥或完整敏感数据。  
   - 错误信息不应该向最终用户泄露内部细节。

### 输出格式
完成安全审查后，必须输出：

```markdown
## 安全审查摘要
- 发现密钥：是 / 否（如有请列出）
- 高风险问题：...
- 中风险问题：...
- 建议：...
- 残留风险：低 / 中 / 高
```
