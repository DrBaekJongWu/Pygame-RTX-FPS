var S=(o,e,r)=>`
    <div class="noHover">
    ${o}
    </div>
    <vscode-divider></vscode-divider>
    <section class="component-container">
        <div>Project Name</div>
        <vscode-text-field id="projectNameInput" class="custom-textfield" placeHolder="myProjectName" value=""></vscode-text-field>
        <i id="projectName-infoText" > </i>

    </section>
    <section class="component-container">
        <vscode-text-area id="projectDescriptionInput" class="custom-textarea" placeHolder="Write your project description here . . ." value="">Description</vscode-text-field>

    </section>
    <section class="component-container">
        <div>Location</div>
        <section class="project-path-row">
            <vscode-text-field id="projectHomePathInput" class="custom-textfield" placeHolder="Path to my project" value="${r}"></vscode-text-field>
            <vscode-button id="browseProjectPathBtn" class="space-left"  appearance="secondary">Browse</vscode-button>
        </section>
        <div id="infoText-projecHomePath" ></div>
    </section>



`,C=(o,e,r)=>`
    <div class="noHover">
    ${o}
    </div>
    <vscode-divider></vscode-divider>
    <section class="component-container">
        <div>Project Name</div>
        <vscode-text-field id="projectNameInput" class="custom-textfield" placeHolder="myProjectName" value=""></vscode-text-field>
        <i id="projectName-infoText" > </i>

    </section>
    <section class="component-container">
        <vscode-text-area id="projectDescriptionInput" class="custom-textarea" placeHolder="Write your project description here . . ." value="">Description</vscode-text-field>

    </section>
    <section class="component-container">
        <div>Location</div>
        <section class="project-path-row">
            <vscode-text-field id="projectHomePathInput" class="custom-textfield" placeHolder="Path to my project" value="${r}"></vscode-text-field>
            <vscode-button id="browseProjectPathBtn" class="space-left"  appearance="secondary">Browse</vscode-button>
        </section>
        <div id="infoText-projecHomePath" ></div>
    </section>
`;window.addEventListener("load",E);function E(){let o=acquireVsCodeApi(),e={pageId:1,index:-1,language:"",language_index:-1,platform:"",platform_index:-1,project_index:-1,osType:""},r=$("#searchInput"),s=$("#createBtn"),l=$("#backBtn"),L=$("#cancelBtn"),d=$("#contentWindow"),n=$(".row"),m=w(),b=m,H,u=[],i=!0,j=!0;l.show(),s.show();let p=a=>{switch(a){case 1:o.postMessage({type:"getPlatformList"}),o.postMessage({type:"getOSType"});break;case 2:console.log("getMain Html content",a),o.postMessage({type:"getLanguageList"});break;case 3:console.log("getMain Html content",a),o.postMessage({type:"getProjectList",platform_index:e.platform_index,language_index:e.language_index});break;case 4:console.log("getMain Html content",a),o.postMessage({type:"getProjectHtml",platform_index:e.platform_index,language_index:e.language_index,project_index:e.project_index});break}},f=a=>{switch(e.index=-1,e.pageId=a,a){case 1:$("#contentInstruction").html("Select a Project Platform"),n=$(".row"),n.on("click",v),s.attr("disabled","true"),l.attr("disabled","true"),d.css("overflow-y","hidden"),$("#search").hide();break;case 2:$("#contentInstruction").html("Select a Project Language"),n=$(".row"),n.on("click",v),l.removeAttr("disabled"),d.css("overflow-y","hidden"),$("#search").hide();break;case 3:$("#contentInstruction").html("Select an Example Project"),n=$(".row"),n.on("click",v),s.attr("disabled","true"),r=$("#searchInput"),r.on("input",()=>{console.log(r.val()),y()}),m=w(),$("#search").show(),d.css("overflow-y","auto");break;case 4:$("#contentInstruction").html("Project Settings"),$("#projectNameInput").on("input",x),$("#projectHomePathInput").on("input",k),$("#search").hide(),d.css("overflow-y","auto"),$("#projectHomePathInput").on("focusout",t=>{let c=$("#projectHomePathInput").val().toString();o.postMessage({type:"updateAndCheckFolderListAtPath",path:c})}),H=$("#browseProjectPathBtn"),H.on("click",T),s.removeAttr("disabled"),l.attr("width","0px"),l.attr("font","0px"),o.postMessage({type:"projectHomePath",index:e.project_index});break}},v=a=>{switch(console.log("projectList CLicked"),e.index=n.index(a.currentTarget),console.log(e.index),e.pageId){case 1:e.index!==-1&&(e.platform_index=e.index,console.log(e.pageId,e.pageId,e.index,"next button click",a),p(2));break;case 2:e.index!==-1&&(e.language_index=e.index,console.log(e.pageId,e.pageId,e.index,"next button click",a),p(3));break;case 3:e.index!==-1&&(e.project_index=e.index,p(4));break;case 4:break;case 5:break}},T=a=>{console.log("browsebtn clicked"),o.postMessage({type:"browseBtn"})},P=a=>a&&i&&j?(s.removeAttr("disabled"),!0):(s.attr("disabled","true"),!1),x=a=>{let t=$("#projectNameInput"),c=$("#projectName-infoText"),h=t.val().toString(),g="";console.log(u),_(h)?(g=" Error: Invalid project name. No special characters allowed.",i=!1):h===""?(g=" Error: Invalid project name. Enter project name.",i=!1):u.includes(h)?(g=" Error: Invalid project name. Project already exist.",i=!1):(i=!0,t.removeClass("errorBorder"),I(c),P(!0)),i?(i=!0,t.removeClass("errorBorder"),I(c),P(!0)):(t.addClass("errorBorder"),M(c,g),P(!1))},k=a=>{let t=$("#projectHomePathInput").val().toString(),c=t.length?t[t.length-1]:"";console.log("project Path",t),B(t,e)?($("#projectHomePathInput").addClass("errorBorder"),M($("#infoText-projecHomePath")," Error: Invalid project path."),j=!1,P(!1)):(c==="\\"||c==="/")&&!a||($("#projectHomePathInput").removeClass("errorBorder"),I($("#infoText-projecHomePath")),j=!0,P(!0))},D=()=>{let a=$("#projectNameInput"),t=$("#projectDescriptionInput"),c=$("#projectHomePathInput"),h=$("#sdkDD");x(),k();let g=i&&j;console.log(g),g?o.postMessage({type:"createProject",simple_project_settings:{project_index:e.project_index,platform_index:e.platform_index,language_index:e.language_index,name:a.val(),description:t.val(),projectPath:c.val().toString(),sdkVersion:h.val()}}):e.pageId=4};n.on("click",v),s.on("click",a=>{switch(e.pageId){case 4:o.postMessage({type:"updateAndCheckFolderListAtPathFinal",path:$("#projectHomePathInput").val().toString()}),e.pageId=5;break;case 5:break}}),l.on("click",a=>{switch(e.pageId){case 1:break;case 2:p(1);break;case 3:p(2);break;case 4:p(3);break;case 5:break}console.log("Back btn clicked")}),L.on("click",a=>{console.log("Cancel btn clicked"),o.postMessage({type:"cancelBtn"})}),window.addEventListener("message",a=>{let t=a.data;switch(console.log("JS Recieved Data",a),t.type){case"browseBtn":case"folderPath":console.log("folder Path Recieved",t.path),$("#projectHomePathInput").val(t.path),o.postMessage({type:"updateAndCheckFolderListAtPath",path:t.path});break;case"updateAndCheckFolderListAtPath":u=t.paths,x();break;case"updateFolderListAtPath":u=t.paths;break;case"updateAndCheckFolderListAtPathFinal":u=t.paths,D();break;case"sdkOptions":console.log(t.sdkOptions),$("#sdkDD").html(t.sdkOptions.toString());break;case"projectHomePath":console.log("projectHomePath",t.projectHomePath),$("#projectHomePathInput").val(t.projectHomePath),o.postMessage({type:"updateFolderListAtPath",path:t.projectHomePath});break;case"getLanguageList":console.log("Language HTML",t.html),$("#contentWindow").html(t.html),f(2);break;case"getPlatformList":console.log("Platform HTML"),$("#contentWindow").html(t.html),f(1);break;case"getProjectList":console.log("Project HTML",t.html),$("#contentWindow").html(t.html),f(3);break;case"getProjectHtml":console.log("Project HTML",t.html),t.language==="cpp"&&$("#contentWindow").html(S(t.html,"","")),t.language==="python"&&$("#contentWindow").html(C(t.html,"","")),f(4);break;case"getSelectedLanguage":e.language=t.language;break;case"getSelectedPlatform":e.platform=t.platform;break;case"getOSType":console.log("OS",t.osType),e.osType=t.osType;break}}),r.on("input",()=>{y()}),p(1);let y=()=>{let a=r.val().toString().toLowerCase();m.forEach(t=>{t.containSelector.hide()}),m.forEach(t=>{t.title.includes(a)||t.description.includes(a)||t.tags.some(c=>c.includes(a))?(console.log("show"),t.containSelector.show()):(console.log("hide"),t.containSelector.hide())})}}function w(){let o=[],e=$(".row");for(let r=0;r<e.children().length;r++){let s=$(`#project-title-${r}`),l=$(`#project-description-${r}`),L=$(`#project-tags-${r}`).children().toArray(),d=[];L.forEach(b=>{d.push(b.innerText.toLowerCase())});let n=s.text().toLowerCase(),m=l.text().toLowerCase();o.push({containSelector:$(e.children()[r]),title:n,description:m,tags:d,index:r})}return console.log("project list",o,e.children()),o}function M(o,e){o.val().toString()!==e&&(o.html(e),o.addClass(["errorMsg","codicon","codicon-error"]))}function I(o){o.removeClass(["errorMsg","codicon","codicon-error"]),o.html("")}function _(o){return/[ `!@#$%^&*()+\=\[\]{};':"\\|,.<>\/?~]/.test(o)}function B(o,e){return console.log("PageInfo",e),e.osType==="Windows_NT"?o.includes("\\\\")||o.includes("//"):e.osType==="Darwin"||e.osType==="Linux"?o.includes("\\"):!1}
//# sourceMappingURL=newProject.js.map
