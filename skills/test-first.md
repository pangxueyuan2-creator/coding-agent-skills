# Test-First Skill for AI Coding Agents

Always think about tests before writing implementation code.

## English

### Rules
1. Before writing any production code, describe the test cases that would prove the feature works.
2. Prefer writing the actual test code first when the language and framework allow it.
3. Cover at least:
   - Happy path
   - Edge cases (empty, null, boundary values)
   - Error / failure paths
4. After implementation, run the tests and report the results.
5. Never claim "tests pass" without actually running them (or clearly stating that execution is not possible in the current environment).

### Output when finishing a task
```markdown
## Test Summary
- New tests added: list files / cases
- Tests run: Yes / No
- Result: All passed / Failed (details)
- Coverage notes: ...
```

---

## 中文

### 规则
1. 写任何生产代码之前，先描述能证明功能正确的测试用例。
2. 在语言和框架允许的情况下，优先写测试代码。
3. 至少覆盖：
   - 正常路径
   - 边界情况（空值、null、边界值）
   - 错误 / 失败路径
4. 实现完成后，运行测试并报告结果。
5. 永远不要在没有实际运行的情况下声称「测试通过」（或者明确说明当前环境无法执行）。

### 完成任务时的输出
```markdown
## 测试摘要
- 新增测试：列出文件 / 用例
- 是否运行：是 / 否
- 结果：全部通过 / 失败（详情）
- 覆盖率说明：...
```
