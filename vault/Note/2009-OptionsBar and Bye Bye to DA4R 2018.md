---
num: 2009
date: 2023-09-25
themes: [Pitfall, VersionMigration]
tags: [revit-api, tbc]
---

# OptionsBar and Bye Bye to DA4R 2018

<https://jeremytammik.github.io/tbc/a/2009_optionsbar.html>

```csharp
&lt;ItemGroup&gt; &lt;PackageReference Include="Nice3point.Revit.Api.AdWindows" Version="$(RevitVersion).*"/&gt; &lt;/ItemGroup&gt;
```

```csharp
public static class RibbonController { private static readonly Grid RootGrid; private static ContentPresenter _panelPresenter; private static readonly FrameworkElement InternalToolPanel; static RibbonController() { RootGrid = VisualUtils.FindVisualParent&lt;Grid&gt;(ComponentManager.Ribbon, "rootGrid"); if (RootGrid is null) throw new InvalidOperationException("Cannot find root grid in Revit UI"); InternalToolPanel = VisualUtils.FindVisualChild&lt;DialogBarControl&gt;(RootGrid, string.Empty); if (InternalToolPanel is null) throw new InvalidOperationException("Cannot find internal tool panel in Revit UI"); } public static void ShowOptionsBar(FrameworkElement content) { if (_panelPresenter is not null) { _panelPresenter.Content = content; _panelPresenter.Visibility = Visibility.Visible; InternalToolPanel.Height = 0; return; } _panelPresenter = CreateOptionsBar(); _panelPresenter.Content = content; InternalToolPanel.Height = 0; } public static void HideOptionsBar() { if (_panelPresenter is null) return; _panelPresenter.Content = null; _panelPresenter.Visibility = Visibility.Collapsed; InternalToolPanel.Height = 26; } private static ContentPresenter CreateOptionsBar() { const int panelRow = 2; RootGrid.RowDefinitions.Insert(2, new RowDefinition { Height = new GridLength(1, GridUnitType.Auto) }); foreach (UIElement child in RootGrid.Children) { var row = Grid.GetRow(child); if (row &gt; 1) Grid.SetRow(child, row + 1); } var panelPresenter = new ContentPresenter(); Grid.SetRow(panelPresenter, panelRow); RootGrid.Children.Add(panelPresenter); return panelPresenter; } }
```

```csharp
&lt;StackPanel x:Class="OptionsBar.Views.OptionsView" xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:d="http://schemas.microsoft.com/expression/blend/2008" xmlns:viewModels="clr-namespace:OptionsBar.ViewModels" d:DataContext="{d:DesignInstance Type=viewModels:OptionsViewModel}" mc:Ignorable="d" Background="#FFE5F0D7" Orientation="Horizontal" Height="26" d:DesignWidth="430"&gt; &lt;TextBlock Margin="10 0 0 0" Text="Wall options" VerticalAlignment="Center" /&gt; &lt;Border Width="3" BorderThickness="1 0" BorderBrush="Azure" Background="Gray" Margin="10 0" /&gt; &lt;TextBlock Text="Offset: " VerticalAlignment="Center" /&gt; &lt;TextBox Width="100" Margin="10 1 0 1" VerticalContentAlignment="Center" Text="{Binding Offset, UpdateSourceTrigger=PropertyChanged}" /&gt; &lt;TextBlock Text="Constraint: " Margin="10 0 0 0" VerticalAlignment="Center" /&gt; &lt;ComboBox Width="100" Margin="10 1 0 1" VerticalContentAlignment="Center" SelectedIndex="0" ItemsSource="{Binding Constraints}" /&gt; &lt;/StackPanel&gt;
```

```csharp
public partial class OptionsViewModel : ObservableObject { [ObservableProperty] private double _offset; [ObservableProperty] private string[] _constraints; }
```

```csharp
private OptionsViewModel SetupOptionsBar() { var options = new OptionsViewModel { Offset = 0, Constraints = Document.EnumerateInstances&lt;Level&gt;(BuiltInCategory.OST_Levels).Select(level => level.Name).ToArray() }; var view = new OptionsView(options); RibbonController.ShowOptionsBar(view); return options; }
```
