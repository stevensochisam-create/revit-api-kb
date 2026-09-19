---
type: MacroManager
namespace: Autodesk.Revit.DB.Macros
version: 2024
members: 18
tags: [revit-api, class]
---

# MacroManager

`Autodesk.Revit.DB.Macros.MacroManager` · Revit 2024 · 18 members

| Kind | Member | Since | Signature |
| --- | --- | --- | --- |
| Method | AddModule | 2014 | `public MacroModule AddModule ( ModuleSettings moduleSettings )` |
| Method | Contains | 2014 | `public bool Contains ( MacroModule module )` |
| Method | Dispose | — | `public void Dispose ()` |
| Method | GetApplicationMacroSecurityOptions | 2014 | `public static ApplicationMacroOptions GetApplicationMacroSecurityOptions ( Application application )` |
| Method | GetBasicIEnumerator | — | `internal virtual IEnumerator GetBasicIEnumerator ()` |
| Method | GetDocumentMacroSecurityOptions | 2014 | `public static DocumentMacroOptions GetDocumentMacroSecurityOptions ( Application application )` |
| Method | GetEnumerator | — | `public virtual IEnumerator < MacroModule > GetEnumerator ()` |
| Method | GetMacroManager | — | `` |
| Method | GetMacroManagerIterator | 2014 | `public MacroManagerIterator GetMacroManagerIterator ()` |
| Method | IsDocLvlMacro | 2014 | `public bool IsDocLvlMacro ()` |
| Method | RemoveModule | 2014 | `public void RemoveModule ( MacroModule module )` |
| Method | SetApplicationMacroSecurityOptions | 2014 | `public static void SetApplicationMacroSecurityOptions ( Application application , ApplicationMacroOptions macroOptions )` |
| Method | SetDocumentMacroSecurityOptions | 2014 | `public static void SetDocumentMacroSecurityOptions ( Application application , DocumentMacroOptions macroOptions )` |
| Property | Count | 2014 | `public int Count { get ; }` |
| Property | Folder | 2014 | `public string Folder { get ; }` |
| Property | IsEnabled | 2014 | `public bool IsEnabled { get ; }` |
| Property | IsValidObject | 2014 | `public bool IsValidObject { get ; }` |
| Property | MacroLevel | 2014 | `public MacroLevel MacroLevel { get ; }` |