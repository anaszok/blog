---
title: Learning C# for Revit, step one
description: A tiny example showing how code blocks look on this blog.
date: 2026-10-29
tags: [revit, csharp, automation]
draft: false
---

Before writing any code, check if Revit already does it out of the box. Schedules, filters and View Templates solve a lot of problems with no code at all.

When code *is* the right tool, here is the smallest possible example: count the walls in the model.

```csharp
// Find every wall in the open model and show how many there are
var walls = new FilteredElementCollector(doc)
    .OfClass(typeof(Wall))
    .ToElements();

TaskDialog.Show("Wall count", $"This model has {walls.Count} walls.");
```

The same idea in Python (for pyRevit or Dynamo):

```python
# Find every wall in the open model and count them
walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()
print("This model has {} walls.".format(len(walls)))
```
